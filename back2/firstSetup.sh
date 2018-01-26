#! /bin/sh

sudo -i
yum install python3
yum install python3-pip

rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
yum install nginx
systemctl start nginx.service

servicectl enable nginx.service



