#!/bin/sh

tarantoolctl stop shard1-master
tarantoolctl stop shard2-rep

rm -r /var/lib/tarantool/*
rm -r /var/log/tarantool/*
rm /var/run/tarantool/shard1-master.control
rm /var/run/tarantool/shard2-rep.control
rm /etc/tarantool/instances.available/shard*
rm /usr/share/tarantool/module*
cp -r lua-procedures/* /usr/share/tarantool
cp shard2-rep.lua /etc/tarantool/instances.available/shard2-rep.lua
cp shard1-master.lua /etc/tarantool/instances.available/shard1-master.lua

tarantoolctl start shard1-master
tarantoolctl start shard2-rep
