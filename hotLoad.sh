#! /bin/sh

sudo tarantoolctl stop shard1-rep
sudo tarantoolctl stop shard2-rep
sudo tarantoolctl stop shard1-master
sudo tarantoolctl stop shard2-master

sudo tarantoolctl start shard1-master
sudo tarantoolctl start shard2-master
sudo tarantoolctl start shard1-rep
sudo tarantoolctl start shard2-rep:

cd back/back/aio-server
python3 main.py
