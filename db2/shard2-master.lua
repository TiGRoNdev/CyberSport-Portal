#! /usr/bin/tarantool

box.cfg{
	listen		=	3301,
	log		=	"file:tnt_shard2_master.log",
	log_format	=	"json",
	work_dir	=	"/home/student26/tnt_shard2_master",
	wal_dir         =       "xlogs",
	memtx_dir       =       "snaps",
	vinyl_dir       =       "cold-data",
	username        =       "student26",
	memtx_memory    =       2147483648,
	checkpoint_interval     =       1800,
}


-- Create GAME space
box.schema.space.create('game', {if_not_exists = true})
box.space.game:create_index('primary', {type = 'hash', parts = {1, 'unsigned'}}) -- Column id
box.space.game:create_index('Name', {type = 'hash', parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
-- Column Logo we're not indexing          3
-- Column Description we're not indexing   4


-- Create PLAYER space
box.schema.space.create('player', {if_not_exists = true})
box.space.player:create_index('primary', {type = 'hash', parts = {1, 'unsigned'}}) -- Column id
box.space.player:create_index('Name', {type = 'hash', parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
-- Column Description we're not indexing   3
-- Column Logo we're not indexing          4
box.space.player:create_index('Rating', {type = 'tree', parts = {5, 'unsigned'}}) -- Column Rating_global, it's not unique
box.space.player:create_index('id_game', {type = 'tree', parts = {6, 'unsigned'}}) -- Column id_game, that's id of game whose player is play
box.space.player:create_index('id_team', {type = 'tree', parts = {7, 'unsigned'}}) -- Column id_team, that's id of team whose player is play; if == 1, Player doesn't exist in any team



-- Create TEAM space
box.schema.space.create('team', {if_not_exists = true})
box.space.team:create_index('primary', {type = 'hash', parts = {1, 'unsigned'}}) -- Column id
box.space.team:create_index('Name', {type = 'hash', parts = {{2, 'string', collation = 'unicode_ci'}}}) -- Column Name, it's unique
-- Column Description we're not indexing   3
-- Column Logo we're not indexing          4
box.space.team:create_index('Rating', {type = 'tree', parts = {5, 'unsigned'}}) -- Column Rating_global, it's not unique
box.space.team:create_index('id_game', {type = 'tree', parts = {6, 'unsigned'}}) -- Column id_game, that's id of game whose team is play


-- Create TEAM_MATCH space
box.schema.space.create('team_match', {if_not_exists = true})
box.space.team_match:create_index('primary', {type = 'hash', parts = {1, 'unsigned'}}) -- Column id
box.space.team_match:create_index('id_team', {type = 'tree', parts = {2, 'unsigned'}}) -- Column id_team
box.space.team_match:create_index('add', {type = 'rtree', parts = {3, 'array'}}) -- Column add with ID's of players whose added to team on match
box.space.team_match:create_index('del', {type = 'rtree', parts = {4, 'array'}}) -- Column add with ID's of players whose deleted in team on match
box.space.team_match:create_index('id_match', {type = 'tree', parts = {5, 'unsigned'}}) -- Column id_match, that's id of match which team is play


local cfg = {
	servers = {
                { uri = '192.168.1.45:3301', zone = '1' }, -- Shard1-master
                { uri = '192.168.1.45:3302', zone = '2' }, -- Shard2-slave
                { uri = 'localhost:3301', zone = '3' }, -- Shard2-master
                { uri = 'localhost:3302', zone = '4' }, -- Shard1-slave
	},
        login           =       'student26',
        password        =       'fobloi56',
        redundancy      =       2,
        binary          =       3301,
}

shard = require('shard')
shard.init(cfg)										
