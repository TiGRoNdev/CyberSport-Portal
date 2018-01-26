#! /bin/sh

sudo yum install python3
sudo yum install python3-pip

sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
sudo yum install nginx
sudo systemctl start nginx.service

sudo servicectl enable nginx.service

sudo pip3 install -r requirements.txt
