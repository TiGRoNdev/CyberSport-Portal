-- This is default tarantool initialization file
-- with easy to use configuration examples including
-- replication, sharding and all major features
-- Complete documentation available in:  http://tarantool.org/doc/
--
-- To start this instance please run `systemctl start tarantool@example` or
-- use init scripts provided by binary packages.
-- To connect to the instance, use "sudo tarantoolctl enter example"
-- Features:
-- 1. Database configuration
-- 2. Binary logging and automatic checkpoints
-- 3. Replication
-- 4. Automatinc sharding
-- 5. Message queue
-- 6. Data expiration

-----------------
-- Configuration
-----------------
local shard = require('shard')
local json = require('json')

box.cfg {
    ------------------------
    -- Network configuration
    ------------------------

    -- The read/write data port number or URI
    -- Has no default value, so must be specified if
    -- connections will occur from remote clients
    -- that do not use “admin address”
    listen = '192.168.1.45:3301';
    -- listen = '*:3301';

    -- The server is considered to be a Tarantool replica
    -- it will try to connect to the master
    -- which replication_source specifies with a URI
    -- for example konstantin:secret_password@tarantool.org:3301
    -- by default username is "guest"
    -- replication_source="127.0.0.1:3102";

    --replication = { 'tnt:tnt@192.168.1.45:3301',
    --                'tnt:tnt@192.168.1.152:3302'};

    read_only = false;

    -- The server will sleep for io_collect_interval seconds
    -- between iterations of the event loop
    io_collect_interval = nil;

    -- The size of the read-ahead buffer associated with a client connection
    readahead = 16320;

    ----------------------
    -- Memtx configuration
    ----------------------

    -- An absolute path to directory where snapshot (.snap) files are stored.
    -- If not specified, defaults to /var/lib/tarantool/INSTANCE
    -- memtx_dir = nil;

    -- How much memory Memtx engine allocates
    -- to actually store tuples, in bytes.
    memtx_memory = 2048 * 1024 * 1024; -- 128Mb

    -- Size of the smallest allocation unit, in bytes.
    -- It can be tuned up if most of the tuples are not so small
    memtx_min_tuple_size = 16;

    -- Size of the largest allocation unit, in bytes.
    -- It can be tuned up if it is necessary to store large tuples
    memtx_max_tuple_size = 128 * 1024 * 1024; -- 128Mb

    -- Reduce the throttling effect of box.snapshot() on
    -- INSERT/UPDATE/DELETE performance by setting a limit
    -- on how many megabytes per second it can write to disk
    -- memtx_snap_io_rate_limit = nil;

    ----------------------
    -- Vinyl configuration
    ----------------------

    -- An absolute path to directory where Vinyl files are stored.
    -- If not specified, defaults to /var/lib/tarantool/INSTANCE
    -- vinyl_dir = nil;

    -- How much memory Vinyl engine can use for in-memory level, in bytes.
    vinyl_memory = 2048 * 1024 * 1024; -- 128Mb

    -- How much memory Vinyl engine can use for caches, in bytes.
    vinyl_cache = 128 * 1024 * 1024; -- 128Mb

    -- Size of the largest allocation unit, in bytes.
    -- It can be tuned up if it is necessary to store large tuples
    vinyl_max_tuple_size = 128 * 1024 * 1024; -- 128Mb

    -- The maximum number of background workers for compaction.
    vinyl_write_threads = 2;

    ------------------------------
    -- Binary logging and recovery
    ------------------------------

    -- An absolute path to directory where write-ahead log (.xlog) files are
    -- stored. If not specified, defaults to /var/lib/tarantool/INSTANCE
    -- wal_dir = nil;

    -- Specify fiber-WAL-disk synchronization mode as:
    -- "none": write-ahead log is not maintained;
    -- "write": fibers wait for their data to be written to the write-ahead log;
    -- "fsync": fibers wait for their data, fsync follows each write;
    wal_mode = "write";

    -- The maximal size of a single write-ahead log file
    wal_max_size = 1024 * 1024 * 1024;

    -- The interval between actions by the checkpoint daemon, in seconds
    checkpoint_interval = 60 * 60; -- one hour

    -- The maximum number of checkpoints that the daemon maintans
    checkpoint_count = 6;

    -- Don't abort recovery if there is an error while reading
    -- files from the disk at server start.
    force_recovery = true;

    ----------
    -- Logging
    ----------

    -- How verbose the logging is. There are six log verbosity classes:
    -- 1 – SYSERROR
    -- 2 – ERROR
    -- 3 – CRITICAL
    -- 4 – WARNING
    -- 5 – INFO
    -- 6 – VERBOSE
    -- 7 – DEBUG
    log_level = 5;

    -- By default, the log is sent to /var/log/tarantool/INSTANCE.log
    -- If logger is specified, the log is sent to the file named in the string
    -- logger = "example.log";

    -- If true, tarantool does not block on the log file descriptor
    -- when it’s not ready for write, and drops the message instead
    log_nonblock = true;

    -- If processing a request takes longer than
    -- the given value (in seconds), warn about it in the log
    too_long_threshold = 0.5;

    -- Inject the given string into server process title
    -- custom_proc_title = 'example';
}

local function bootstrap()
    -- local space = box.schema.create_space('example')
    -- space:create_index('primary')
    -- Comment this if you need fine grained access control (without it, guest
    -- will have access to everything)
    -- box.schema.user.grant('guest', 'read,write,execute', 'universe')

    box.schema.space.create('cup', {if_not_exists = true})
    box.space.cup:create_index('primary', {type = 'hash', if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    --box.space.cup:create_index('Name', {type = 'hash', if_not_exists = true, parts = {2, 'string'}}) -- Column Name, it's unique
    --box.space.cup:create_index('Logo', {type = 'tree', if_not_exists = true, parts = {3, 'string'}}) -- Column Logo, it's not unique
    -- Column Description we're not indexing
    box.space.cup:create_index('Rating', {type = 'tree', unique = false,  if_not_exists = true, parts = {5, 'unsigned'}}) -- Column Rating_of_cup, it's not unique
    box.space.cup:create_index('id_game', {type = 'tree', unique = false, if_not_exists = true, parts = {6, 'unsigned'}}) -- Column id_game, it's not unique
    
    -- Create CUP_STAGE space
    box.schema.space.create('stage', {if_not_exists = true})
    box.space.stage:create_index('primary', {type = 'hash', if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    box.space.stage:create_index('Type', {type = 'tree', unique = false, if_not_exists = true, parts = {2, 'unsigned'}}) -- Column Type_of_stage, it's not unique = 0 .. 0.25 .. 1
    box.space.stage:create_index('Start', {type = 'rtree', unique = false, if_not_exists = true, parts = {3, 'array'}}) -- Column Start_of_stage, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    box.space.stage:create_index('End', {type = 'rtree', unique = false, if_not_exists = true, parts = {4, 'array'}}) -- Column End_of_stage, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    -- Column Description we aren't indexing
    box.space.stage:create_index('id_cup', {type = 'tree', unique = false, if_not_exists = true, parts = {6, 'unsigned'}}) -- Columd for Foreign Key (id of CUP), it's not unique

    -- Create MATCH space
    box.schema.space.create('match', {if_not_exists = true})
    box.space.match:create_index('primary', {type = 'hash', if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
    box.space.match:create_index('Start', {type = 'rtree', unique = false, if_not_exists = true, parts = {2, 'array'}}) -- Column Start_of_match, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    -- box.space.match:create_index('Status', {type = 'tree', if_not_exists = true, parts = {3, 'string'}}) -- Column Status, it's not unique
    -- Column Name we're not indexing               4
    -- Column Description we're not indexing        5
    -- Column Logo we're not indexing               6
    -- Column URI_VIDEOFILE we're not indexing      7
    box.space.match:create_index('id_stage', {type = 'tree', unique = false, if_not_exists = true, parts = {8, 'unsigned'}}) -- Column id_stage (for Foreign key), it's not unique

    -- Keep things safe by default
    box.schema.user.create('tnt', { password = 'tnt' })
    --  box.schema.user.grant('example', 'replication')
    box.schema.user.grant('tnt', 'read,write,execute', 'universe')
    print("box.once is executed on master")
end

-- for first run create a space and add set up grants
box.once('SHARD-1-MASTER', bootstrap)

-----------------------
-- Automatinc sharding
-----------------------
-- N.B. you need install tarantool-shard package to use shadring
-- Docs: https://github.com/tarantool/shard/blob/master/README.md
-- Example:
shard.init {
    servers = {
        { uri = [[192.168.1.45:3301]]; zone = [[0]]; };
        { uri = [[192.168.1.152:3302]]; zone = [[1]]; };
	{ uri = [[192.168.1.152:4301]]; zone = [[1]]; };
	{ uri = [[192.168.1.45:4302]]; zone = [[0]]; };
    };
    login = 'tnt';
    password = 'tnt';
    redundancy = 2;
    binary = '192.168.1.45:3301';
    monitor = true;
    replication = true;
}

shard.cup:insert({1, 'International 2012', '/static/img/logo/int12.png', "That's International Championship on Dota 2", 10, 1})
print(json.encode(shard.cup:select({1})))

-----------------
-- Message queue
-----------------
-- N.B. you need to install tarantool-queue package to use queue
-- Docs: https://github.com/tarantool/queue/blob/master/README.md
-- Example:
queue = require('queue')
queue.create_tube('shard1_queue', 'fifottl', {temporary = true})

-------------------
-- Data expiration
-------------------
-- N.B. you need to install tarantool-expirationd package to use expirationd
-- Docs: https://github.com/tarantool/expirationd/blob/master/README.md
-- Example (deletion of all tuples):
--  local expirationd = require('expirationd')
--  local function is_expired(args, tuple)
--    return true
--  end
--  expirationd.start("clean_all", space.id, is_expired {
--    tuple_per_item = 50,
--    full_scan_time = 3600
--  })
