#! /bin/sh

 # Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
    echo "!!!!!!!!!!!!!!!             WARNING: This script must be run as root; MUST (sudo -i) NOT sudo preffix                   !!!!!!!!!!!!!!!!!!!"
    exit 1
fi

sudo cp back/config/nginx.conf /etc/nginx/nginx.conf
sudo cp -r back/config/conf.d /etc/nginx/

echo ""
echo "!!!!!!!!!!!!!!!!!!!!!!!!!                              YOU MUST CHANGE IP-adress of second backend machine in upstream                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo ""
echo "Wait for open cofiguration file..."
sleep 8s

cd /etc/nginx/conf.d
sudo vim default.conf

sudo systemctl restart nginx.service
sudo systemctl enable nginx.service

sudo cat /var/log/audit/audit.log | grep nginx | grep denied | audit2allow -M mynginx
semodule -i mynginx.pp
