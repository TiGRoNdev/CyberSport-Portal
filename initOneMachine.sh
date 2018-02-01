echo "______________________		Installing Tarantool 1.7 and modules(queue, shard, pool)		________________________________"
echo

sudo apt-get install curl

curl http://download.tarantool.org/tarantool/1.7/gpgkey | sudo apt-key add -
release=`lsb_release -c -s`

# install https download transport for APT
sudo apt-get -y install apt-transport-https

# append two lines to a list of source repositories
sudo rm -f /etc/apt/sources.list.d/*tarantool*.list
sudo echo "deb http://download.tarantool.org/tarantool/1.7/ubuntu/ $release main" > /etc/apt/sources.list.d/tarantool_1_7.list
sudo echo "deb-src http://download.tarantool.org/tarantool/1.7/ubuntu/ $release main" >> /etc/apt/sources.list.d/tarantool_1_7.list

# install
sudo apt-get update
sudo apt-get -y install tarantool
sudo apt-get install tarantool-queue tarantool-shard tarantool-pool

echo
echo "_______________________		Tarantool and modules successfully installed!		____________________________"
echo


