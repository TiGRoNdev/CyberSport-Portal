systemctl stop tarantool@shard1-slave.service
systemctl stop tarantool@shard2-master.service

rm -r /var/lib/tarantool/*
rm -r /var/log/tarantool/*
rm /var/run/tarantool/shard2-master.control
rm /var/run/tarantool/shard1-slave.control
rm /etc/tarantool/instances.available/shard*
cp shard2-master.lua /etc/tarantool/instances.available/shard2-master.lua
cp shard1-slave.lua /etc/tarantool/instances.available/shard1-slave.lua

tarantoolctl start shard2-master
tarantoolctl start shard1-slave
