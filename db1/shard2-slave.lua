#! /usr/bin/tarantool


box.cfg{
	listen		=	3302,
	replication	=	"student26:fobloi56@192.168.1.152:3301",
	read_only	=	"true",
	log		=	"file:tnt_shard2_slave.log",
	log_format	=	"json",
	work_dir	=	"/home/student26/tnt_shard2_slave",
	wal_dir		=	"xlogs",
	memtx_dir	=	"snaps",
	vinyl_dir	=	"cold-data",
	username	=	"student26",
	memtx_memory	=	2147483648,
	checkpoint_interval	=	1800
}

-- Create USER for db
box.schema.user.create('student26', {password = 'fobloi56'})
box.schema.user.grant('student26', 'read,write,execute', 'universe')

local cfg = {
	servers = {
		{ uri = 'localhost:3301', zone = '1' }, -- Shard1-master
		{ uri = 'localhost:3302', zone = '2' }, -- Shard2-slave
		{ uri = '192.168.1.152:3301', zone = '3' }, -- Shard2-master
		{ uri = '192.168.1.152:3302', zone = '4' }, -- Shard1-slave
	},
	login		=	'student26',
	password	=	'fobloi56',
	redundancy	=	'2',
	binary		=	3302,
}

shard = require('shard')
shard.init(cfg)
