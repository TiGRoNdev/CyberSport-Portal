#! /bin/sh

sudo yum update

sudo yum install yum-utils wget gcc gcc-c++ kernel-devel pcre-devel openssl-devel GeoIP-devel libxslt-devel
sudo yum groupinstall development

sudo yum install vim iotop
sudo yum install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum install python36u supervisor

sudo yum install python36u-pip
sudo yum install python36u-devel

sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
sudo yum install nginx

sudo systemctl start nginx.service

sudo servicectl enable nginx.service

sudo pip3.6 install -r requirements.txt

./setConfigs.sh
