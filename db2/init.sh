rm -r /var/lib/tarantool/*
rm -r /var/log/tarantool/*
cp shard1-slave.lua /etc/tarantool/instances.available/shard1-slave.lua
tarantoolctl start shard1-slave
