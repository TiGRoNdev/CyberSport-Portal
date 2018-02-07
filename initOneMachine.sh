#!/bin/sh

cd oneMachine
sudo cp .env ../back/back/aio-server/.env
sudo ./init.sh
echo
echo
cd ../back/back/aio-server
python3 main.py
