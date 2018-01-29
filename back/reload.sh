#! /bin/sh

 # Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
    echo "!!!!!!!!!!!!!!!             WARNING: This script must be run as root; MUST (sudo -i) NOT sudo preffix                   !!!!!!!!!!!!!!!!!!!"
    exit 1
fi
supervisorctl status
sleep 3s

echo
supervisorctl restart aio:*
echo

curl localhost
echo
echo

cat /var/log/audit/audit.log | grep nginx | grep denied | audit2allow -M mynginx
semodule -i mynginx.pp

chown nginx /tmp/aio_1.sock
chown nginx /tmp/aio_2.sock

curl localhost
