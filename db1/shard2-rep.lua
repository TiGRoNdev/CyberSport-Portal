local shard = require('shard')
box.cfg {
    listen = '192.168.1.45:3302';
    replication = 'tnt:tnt@192.168.1.152:3301';
    io_collect_interval = nil;
    readahead = 16320;
    memtx_memory = 1500 * 1024 * 1024; -- 128Mb
    memtx_min_tuple_size = 16;
    memtx_max_tuple_size = 128 * 1024 * 1024; -- 128Mb
    vinyl_memory = 2048 * 1024 * 1024; -- 128Mb
    vinyl_cache = 128 * 1024 * 1024; -- 128Mb
    vinyl_max_tuple_size = 128 * 1024 * 1024; -- 128Mb
    vinyl_write_threads = 2;
    wal_mode = "none";
    wal_max_size = 256 * 1024 * 1024;
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

    box.schema.user.create('tnt', { password = 'tnt', if_not_exists = true})
end

box.once('SHARD-2-REPLICA', bootstrap)

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
    binary = '192.168.1.45:3302';
    monitor = false;
    replication = true;
}