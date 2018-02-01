cd /home/student26
mkdir tnt_shard2_master
cd tnt_shard2_master
mkdir xlogs
mkdir snaps
mkdir cold-data
touch tnt_shard2_master.log

cd /home/student26
mkdir tnt_shard1_slave
cd tnt_shard1_slave
mkdir xlogs
mkdir snaps
mkdir cold-data
touch tnt_shard1_slave.log

cd /home/student26/CyperSport-portal/db2

./shard2-master.lua
./shard1-slave.lua
