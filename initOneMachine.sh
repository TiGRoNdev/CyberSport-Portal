#!/bin/sh

cd oneMachine
sudo ./init.sh
echo
echo
cd ../back/back/aio-server
python3 main.py
