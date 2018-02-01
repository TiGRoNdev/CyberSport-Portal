#! /usr/bin/tarantool


box.cfg{
	listen		=	3301,
	log             =       "file:tnt_shard1_master.log",
	log_format      =       "json",
	work_dir	=	"/home/student26/tnt_shard1_master",
	wal_dir		=	"xlogs",
	memtx_dir	=	"snaps",
	vinyl_dir	=	"cold-data",
	username	=	"student26",
	memtx_memory	=	2147483648,
	checkpoint_interval	=	1800,
	replication	=	{'replicator:pass@localhost:3301',
				 'replicator:pass@192.168.1.152:3302'},
	read_only	=	false
}

box.schema.user.create('replicator', {password = 'pass', if_not_exists = true})
box.schema.user.grant('replicator', 'replication', {if_not_exists = true}) -- grant replication role

-- Create CUP space
box.schema.space.create('cup', {if_not_exists = true})
box.space.cup:create_index('primary', {type = 'hash', if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
box.space.cup:create_index('Name', {type = 'hash', if_not_exists = true, parts = {2, 'string'}}) -- Column Name, it's unique
box.space.cup:create_index('Logo', {type = 'tree', if_not_exists = true, parts = {3, 'string'}}) -- Column Logo, it's not unique
-- Column Description we're not indexing
box.space.cup:create_index('Rating', {type = 'tree', if_not_exists = true, parts = {5, 'unsigned'}}) -- Column Rating_of_cup, it's not unique
box.space.cup:create_index('id_game', {type = 'tree', if_not_exists = true, parts = {6, 'unsigned'}}) -- Column id_game, it's not unique

-- Create USER for db
box.schema.user.create('student26', {password = 'fobloi56', if_not_exists = true})

-- Create CUP_STAGE space
box.schema.space.create('stage', {if_not_exists = true})
box.space.stage:create_index('primary', {type = 'hash', if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
box.space.stage:create_index('Type', {type = 'tree', if_not_exists = true, parts = {2, 'unsigned'}}) -- Column Type_of_stage, it's not unique = 0 .. 0.25 .. 1
box.space.stage:create_index('Start', {type = 'rtree', if_not_exists = true, parts = {3, 'array'}}) -- Column Start_of_stage, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
box.space.stage:create_index('End', {type = 'rtree', if_not_exists = true, parts = {4, 'array'}}) -- Column End_of_stage, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
-- Column Description we aren't indexing
box.space.stage:create_index('id_cup', {type = 'tree', if_not_exists = true, parts = {6, 'unsigned'}}) -- Columd for Foreign Key (id of CUP), it's not unique


-- Create MATCH space
box.schema.space.create('match', {if_not_exists = true})
box.space.match:create_index('primary', {type = 'hash', if_not_exists = true, parts = {1, 'unsigned'}}) -- Column id
box.space.match:create_index('Start', {type = 'rtree', if_not_exists = true, parts = {2, 'array'}}) -- Column Start_of_match, it's not unique, DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
box.space.match:create_index('Status', {type = 'tree', if_not_exists = true, parts = {3, 'string'}}) -- Column Status, it's not unique
-- Column Name we're not indexing		4
-- Column Description we're not indexing	5
-- Column Logo we're not indexing		6
-- Column URI_VIDEOFILE we're not indexing	7
box.space.match:create_index('id_stage', {type = 'tree', if_not_exists = true, parts = {8, 'unsigned'}}) -- Column id_stage (for Foreign key), it's not unique


local cfg = {
	servers = {
		{ uri = 'localhost:3301', zone = '3' }, -- Shard1-master
		{ uri = 'localhost:3302', zone = '4' }, -- Shard2-slave
		{ uri = '192.168.1.152:3301', zone = '1' }, -- Shard2-master
		{ uri = '192.168.1.152:3302', zone = '2' }, -- Shard1-slave
	},
	login		=	'student26',
	password	=	'fobloi56',
	redundancy	=	2,
	binary		=	3301,
}

shard = require('shard')
shard.init(cfg)
