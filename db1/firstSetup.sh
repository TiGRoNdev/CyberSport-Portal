#! /bin/sh

sudo yum update

sudo yum install yum-utils
sudo yum groupinstall development

sudo yum install vim iotop

# Clean up yum cache
sudo yum clean all

# Enable EPEL repository
sudo yum -y install http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo sed 's/enabled=.*/enabled=1/g' -i /etc/yum.repos.d/epel.repo

# Add Tarantool repository
sudo rm -f /etc/yum.repos.d/*tarantool*.repo
sudo tee /etc/yum.repos.d/tarantool_1_7.repo <<- EOF
[tarantool_1_7]
name=EnterpriseLinux-7 - Tarantool
baseurl=http://download.tarantool.org/tarantool/1.7/el/7/x86_64/
gpgkey=http://download.tarantool.org/tarantool/1.7/gpgkey
repo_gpgcheck=1
gpgcheck=0
enabled=1

[tarantool_1_7-source]
name=EnterpriseLinux-7 - Tarantool Sources
baseurl=http://download.tarantool.org/tarantool/1.7/el/7/SRPMS
gpgkey=http://download.tarantool.org/tarantool/1.7/gpgkey
repo_gpgcheck=1
gpgcheck=0
EOF

# Update metadata
sudo yum makecache -y --disablerepo='*' --enablerepo='tarantool_1_7' --enablerepo='epel'

# Install Tarantool
sudo yum -y install tarantool


#INSTALLING Tarantool is DONE


#----> NEXT STEP --->

sudo yum install tarantool-queue tarantool-shard tarantool-pool tarantool-expirationd
