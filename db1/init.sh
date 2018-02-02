systemctl stop tarantool@shard1-master.service
systemctl stop tarantool@shard2-rep.service

rm -r /var/lib/tarantool/*
rm -r /var/log/tarantool/*
rm /var/run/tarantool/shard1-master.control
rm /var/run/tarantool/shard2-rep.control
rm /etc/tarantool/instances.available/shard*
cp shard2-rep.lua /etc/tarantool/instances.available/shard2-rep.lua
cp shard1-master.lua /etc/tarantool/instances.available/shard1-master.lua

tarantoolctl start shard1-master
tarantoolctl start shard2-rep
