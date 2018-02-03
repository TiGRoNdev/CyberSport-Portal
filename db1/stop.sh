#! /bin/sh

tarantoolctl stop shard1-master
tarantoolctl stop shard2-rep

echo
echo
echo "-----------------------------------------   LOG of SHARD-1-MASTER  -----------------------------------"
echo
echo
cat /var/log/tarantool/shard1-master.log
echo
echo
echo "-----------------------------------------   LOG of SHARD-2-REPLICA  ----------------------------------"
echo
echo
cat /var/log/tarantool/shard2-rep.log
