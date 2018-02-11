local shard2 = require('shard')
local json = require('json')

box.cfg {
    read_only = false;
    io_collect_interval = nil;
    readahead = 16320;
    memtx_memory = 2048 * 1024 * 1024; -- 128Mb
    memtx_min_tuple_size = 16;
    memtx_max_tuple_size = 128 * 1024 * 1024; -- 128Mb
    vinyl_memory = 2048 * 1024 * 1024;
    vinyl_cache = 128 * 1024 * 1024;
    vinyl_max_tuple_size = 128 * 1024 * 1024;
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

local function bootstrap2()
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

    game = box.schema.space.create('game', {if_not_exists = true})
    game:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    game:create_index('name', {type = 'tree', unique = true, if_not_exists = true, parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
    -- Column Logo we're not indexing          3
    -- Column Description we're not indexing   4
    game:format({
                   {name='id', type='unsigned'},
                   {name='name', type='string'},
                   {name='logo', type='string'},
                   {name='description', type='string'},
               })


    -- Create PLAYER space
    player = box.schema.space.create('player', {if_not_exists = true})
    player:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    player:create_index('name', {type = 'tree', unique = true, if_not_exists = true, parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
    -- Column Description we're not indexing   3
    -- Column Logo we're not indexing          4
    player:create_index('rating', {type = 'tree', unique = false,  if_not_exists = true, parts = {5, 'unsigned'}}) -- Column Rating_global, it's not unique
    player:create_index('id_game', {type = 'tree', unique = false, if_not_exists = true, parts = {6, 'unsigned'}}) -- Column id_game, that's id of game whose player is play
    player:create_index('id_team', {type = 'tree', unique = false, if_not_exists = true, parts = {7, 'unsigned'}}) -- Column id_team, that's id of team whose player is play; if == 1, Player doesn't exist in any team
    player:format({
                   {name='id', type='unsigned'},
                   {name='name', type='string'},
                   {name='description', type='string'},
                   {name='logo', type='string'},
                   {name='rating', type='unsigned'},
                   {name='id_game', type='unsigned'},
                   {name='id_team', type='unsigned'},
               })


    -- Create TEAM space
    team = box.schema.space.create('team', {if_not_exists = true})
    team:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    team:create_index('name', {type = 'tree', unique = true, if_not_exists = true, parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
    -- Column Description we're not indexing   3
    -- Column Logo we're not indexing          4
    team:create_index('rating', {type = 'tree', unique = false, if_not_exists = true, parts = {5, 'unsigned'}}) -- Column Rating_global, it's not unique
    team:create_index('id_game', {type = 'tree', unique = false, if_not_exists = true, parts = {6, 'unsigned'}}) -- Column id_game, that's id of game whose team is play
    team:create_index('owner', {type = 'tree', unique = false, if_not_exists = true, parts = {7, 'unsigned'}}) -- Column owner, that's id of User who is team manager
    team:format({
                   {name='id', type='unsigned'},
                   {name='name', type='string'},
                   {name='description', type='string'},
                   {name='logo', type='string'},
                   {name='rating', type='unsigned'},
                   {name='id_game', type='unsigned'},
                   {name='owner', type='unsigned'}
               })


    -- Create TEAM_MATCH space
    team_match = box.schema.space.create('team_match', {if_not_exists = true})
    team_match:create_index('primary', {type = 'tree', unique = true, if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    team_match:create_index('id_team', {type = 'tree', unique = false, if_not_exists = true, parts = {2, 'unsigned'}}) -- Column id_team
    --box.space.team_match:create_index('add', {type = 'rtree', if_not_exists = true, parts = {3, 'array'}}) -- Column add with ID's of players whose added to team on match
    --box.space.team_match:create_index('del', {type = 'rtree', if_not_exists = true, parts = {4, 'array'}}) -- Column add with ID's of players whose deleted in team on match
    team_match:create_index('id_match', {type = 'tree', unique = false, if_not_exists = true, parts = {5, 'unsigned'}}) -- Column id_match, that's id of match which team is play
    team_match:format({
                   {name='id', type='unsigned'},
                   {name='id_team', type='unsigned'},
                   {name='add', type='array'},
                   {name='del', type='array'},
                   {name='id_match', type='unsigned'},
               })


    -- Keep things safe by default
    box.schema.user.create('tnt', { password = 'tnt', if_not_exists = true })
    -- box.schema.user.grant('example', 'replication')
    box.schema.user.grant('tnt', 'read,write,execute', 'universe', nil, {if_not_exists = true})

    print("box.once is executed on master")
end

box.once('SHARD-2-MASTER-', bootstrap2)

shard2.init {
    servers = {
        { uri = [[192.168.1.152:3302]]; zone = [[0]]; };
        { uri = [[192.168.1.152:3301]]; zone = [[1]]; };
	{ uri = [[192.168.1.45:3301]]; zone = [[2]]; };
	{ uri = [[192.168.1.45:3302]]; zone = [[3]]; };
    };
    login = 'tnt';
    password = 'tnt';
    redundancy = 2;
    binary = '192.168.1.152:3301';
    monitor = false;
    replication = true;
}

shard2.game:insert({1, 'Dota 2', '/static/img/logo/int12.png', "That's most popular online game"})
print(json.encode(shard2.game:select({1})))


queue = require('queue')
queue.create_tube('shard2_queue', 'fifottl', {temporary = true})
