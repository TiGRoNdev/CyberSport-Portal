local shard = require('shard')
local json = require('json')

box.cfg {
    listen = '192.168.1.45:3301';

    read_only = false;
    io_collect_interval = nil;
    readahead = 16320;
    memtx_memory = 2048 * 1024 * 1024; -- 128Mb
    memtx_min_tuple_size = 16;
    memtx_max_tuple_size = 128 * 1024 * 1024; -- 128Mb
    vinyl_memory = 2048 * 1024 * 1024; -- 128Mb
    vinyl_cache = 128 * 1024 * 1024; -- 128Mb
    vinyl_max_tuple_size = 128 * 1024 * 1024; -- 128Mb
    vinyl_write_threads = 2;
    wal_mode = "write";

    wal_max_size = 1024 * 1024 * 1024;
    checkpoint_interval = 60 * 60; -- one hour
    checkpoint_count = 6;
    force_recovery = true;
    log_level = 5;
    log_nonblock = true;
    too_long_threshold = 0.5;
}

local function bootstrap()
    function mod_insert(space_to_insert, tuple)
        space = box.space[space_to_insert]
        tup = space:auto_increment(tuple)
        return tup[1]
    end
    function mod_len(space)
        return box.space[space]:len()
    end
    function mod_search(space_to_search, index, value, iter, lim)
        space = box.space[space_to_search]
        res = space.index[index]:select({value}, {iterator = iter, limit = lim})
        return res
    end
    function mod_update(space_to_update, id, field_no, iter, value)
        space = box.space[space_to_update]
        res = space:update(id, {{iter, field_no, value}})
        return res
    end
    function mod_delete(space_to_delete, id)
        space = box.space[space_to_delete]
        space:delete(id)
    end

    cup = box.schema.space.create('cup', {if_not_exists = true})
    cup:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    cup:create_index('name', {type = 'tree', unique = true, if_not_exists = true, parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
    --box.space.cup:create_index('Logo', {type = 'tree', if_not_exists = true, parts = {3, 'string'}}) -- Column Logo, it's not unique
    -- Column Description we're not indexing
    cup:create_index('rating', {type = 'tree', unique = false,  if_not_exists = true, parts = {5, 'unsigned'}}) -- Column Rating_of_cup, it's not unique
    cup:create_index('id_game', {type = 'tree', unique = false, if_not_exists = true, parts = {6, 'unsigned'}}) -- Column id_game, it's not unique
    cup:create_index('owner', {type = 'tree', unique = false, if_not_exists = true, parts = {7, 'unsigned'}}) -- Column owner, that's id of User who is team manager
    cup:format({
                   {name='id', type='unsigned'},
                   {name='name', type='string'},
                   {name='logo', type='string'},
                   {name='description', type='string'},
                   {name='rating', type='unsigned'},
                   {name='id_game', type='unsigned'},
                   {name='owner', type='unsigned'}
               })

    -- Create CUP_STAGE space
    stage = box.schema.space.create('stage', {if_not_exists = true})
    stage:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    stage:create_index('type', {type = 'tree', unique = false, if_not_exists = true, parts = {2, 'scalar'}}) -- Column Type_of_stage, it's not unique = 0 ..  .. 10
    --stage:create_index('start', {type = 'rtree', unique = false, if_not_exists = true, parts = {3, 'array'}}) -- Column Start_of_stage, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    --stage:create_index('end', {type = 'rtree', unique = false, if_not_exists = true, parts = {4, 'array'}}) -- Column End_of_stage, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    -- Column Description we aren't indexing
    stage:create_index('id_cup', {type = 'tree', unique = false, if_not_exists = true, parts = {6, 'unsigned'}}) -- Columd for Foreign Key (id of CUP), it's not unique
    stage:format({
                   {name='id', type='unsigned'},
                   {name='type', type='scalar'},
                   {name='start', type='array'},
                   {name='end', type='array'},
                   {name='description', type='string'},
                   {name='id_cup', type='unsigned'},
               })

    -- Create MATCH space
    match = box.schema.space.create('match', {if_not_exists = true})
    match:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    --match:create_index('start', {type = 'rtree', unique = false, if_not_exists = true, parts = {2, 'array'}}) -- Column Start_of_match, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    match:create_index('status', {type = 'tree', unique = false, if_not_exists = true, parts = {3, 'string'}}) -- Column Status, it's not unique    -- Column Name we're not indexing               4
    -- Column Description we're not indexing        5
    -- Column Logo we're not indexing               6
    -- Column URI_VIDEOFILE we're not indexing      7
    -- match:create_index('id_winner', {type = 'tree', unique = false, if_not_exists = true, parts = {8, 'unsigned'}}) -- Column id_winner (for Foreign key), it's not unique
    match:create_index('id_stage', {type = 'tree', unique = false, if_not_exists = true, parts = {9, 'unsigned'}}) -- Column id_stage (for Foreign key), it's not unique
    match:format({
                   {name='id', type='unsigned'},
                   {name='start', type='array'},
                   {name='status', type='string'},
                   {name='name', type='string'},
                   {name='description', type='string'},
                   {name='logo', type='string'},
                   {name='uri_video', type='string'},
                   {name='id_winner', type='unsigned'},
                   {name='id_stage', type='unsigned'},
               })

    user = box.schema.space.create('user', {if_not_exists = true})
    user:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    user:create_index('email', {type = 'tree', unique = true, if_not_exists = true, parts = {2, 'string'}}) -- Column email
    -- Column hash we're not indexing
    -- Column salt we're not indexing
    -- Column is_admin we're not indexing
    -- Column is_organizer we're not indexing
    -- Column is_team we're not indexing
    user:format({
                   {name='id', type='unsigned'},
                   {name='email', type='string'},
                   {name='hash', type='string'},
                   {name='salt', type='string'},
                   {name='is_admin', type='boolean'},
                   {name='is_organizer', type='boolean'},
                   {name='is_team', type='boolean'},
               })

    -- Keep things safe by default
    box.schema.user.create('tnt', { password = 'tnt' })
    --  box.schema.user.grant('example', 'replication')
    box.schema.user.grant('tnt', 'read,write,execute', 'universe')
    print("box.once is executed on master")
end

box.once('SHARD-1-MASTER', bootstrap)

shard.init {
    servers = {
        { uri = [[192.168.1.45:3302]]; zone = [[0]]; };
        { uri = [[192.168.1.45:3301]]; zone = [[1]]; };
	{ uri = [[192.168.1.152:3301]]; zone = [[2]]; };
	{ uri = [[192.168.1.152:3302]]; zone = [[3]]; };
    };
    login = 'tnt';
    password = 'tnt';
    redundancy = 2;
    binary = '192.168.1.45:3301';
    monitor = false;
    replication = true;
}

shard.cup:insert({1, 'International 2012', '/static/img/logo/int12.png', "That's International Championship on Dota 2", 10, 1})
print(json.encode(shard.cup:select({1})))

queue = require('queue')
queue.create_tube('shard1_queue', 'fifottl', {temporary = true})
