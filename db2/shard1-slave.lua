#! /usr/bin/tarantool


box.cfg{
	listen		=	3302,
	replication	=	'student26:fobloi56@192.168.1.45:3301',
	read_only	=	true,
	log		=	'file:tnt_shard1_slave.log',
	log_format	=	'json',
	work_dir	=	'/home/student26/tnt_shard1_slave',
	wal_dir		=	'xlogs',
	memtx_dir	=	'snaps',
	vinyl_dir	=	'cold-data',
	username	=	'student26',
	memtx_memory	=	2147483648,
	checkpoint_interval	=	1800,
	replication     =       {'replicator:pass@192.168.1.45:3301',
                                 'replicator:pass@localhost:3302'}
}

box.schema.user.create('replicator', {password = 'pass', if_not_exists = true})
box.schema.user.grant('replicator', 'replication', {if_not_exists = true}) -- grant replication role


-- Create USER for db
box.schema.user.create('student26', {password = 'fobloi56', if_not_exists = true})

local cfg = {
	servers = {
		{ uri = '192.168.1.45:3301', zone = '3' }, -- Shard1-master
		{ uri = '192.168.1.45:3302', zone = '4' }, -- Shard2-slave
		{ uri = 'localhost:3301', zone = '1' }, -- Shard2-master
		{ uri = 'localhost:3302', zone = '2' }, -- Shard1-slave
	},
	login		=	'student26',
	password	=	'fobloi56',
	redundancy	=	2,
	binary		=	3302,
}

shard = require('shard')
shard.init(cfg)
