#! /bin/sh

 # Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
    echo "!!!!!!!!!!!!!!!             WARNING: This script must be run as root; MUST (sudo -i) NOT sudo preffix                   !!!!!!!!!!!!!!!!!!!"
    exit 1
fi

sudo cp back/config/nginx.conf /etc/nginx/nginx.conf
sudo cp -r back/config/conf.d /etc/nginx/
sudo cp back/config/aio.conf /etc/supervisor/conf.d/aio.conf 


cd /usr/local/lib/python3.6/dist-packages/tao1/sites
mv dao daoerp
cd /home/student26/back/back
utils.py -p aio-server
cd aio-server

echo ""
echo "!!!!!!!!!!!!!!!!!!!!!!!!!                        PLEASE CCHANGE settings of YOUR project                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo ""
sleep 5s


vim settings.py
cp /home/student26/back/test-index.py /home/student26/back/back/aio-server/index.py


echo ""
echo "!!!!!!!!!!!!!!!!!!!!!!!!!                        YOUR APP is located in /home/student26/back/back/aio-server/index.py                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo ""
sleep 5s


echo ""
echo "!!!!!!!!!!!!!!!!!!!!!!!!!                              YOU MUST CHANGE CONFIG of SUPERVISOR aiohtpp-server startup                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo ""
echo "Wait for open cofiguration file..."
sleep 8s

vim /etc/supervisor/conf.d/aio.conf

supervisorctl reread
supervisorctl update
echo
echo
supervisorctl status



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
