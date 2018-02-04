#!/bin/sh

systemctl stop tarantool@shard1-rep.service
systemctl stop tarantool@shard2-master.service
systemctl stop tarantool@shard1-master.service
systemctl stop tarantool@shard2-rep.service

rm -r /var/lib/tarantool/*
rm -r /var/log/tarantool/*
rm /var/run/tarantool/shard*
rm /etc/tarantool/instances.enabled/shard*
cp shard2-master.lua /etc/tarantool/instances.enabled/shard2-master.lua
cp shard1-rep.lua /etc/tarantool/instances.enabled/shard1-rep.lua
cp shard1-master.lua /etc/tarantool/instances.enabled/shard1-master.lua
cp shard2-rep.lua /etc/tarantool/instances.enabled/shard2-rep.lua

tarantoolctl start shard1-master
tarantoolctl start shard2-master
tarantoolctl start shard1-rep
tarantoolctl start shard2-rep
