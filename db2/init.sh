rm -r /var/lib/tarantool/*
rm -r /var/log/tarantool/*
rm /var/run/tarantool/shard1-slave.control
rm /etc/tarantool/instances.available/shard*
cp shard1-slave.lua /etc/tarantool/instances.available/shard1-slave.lua
tarantoolctl start shard1-slave
