#!/bin/bash

echo "Install dependencies [python]"
cat requirements.txt
sudo pip3 install -r requirements.txt
echo

echo "Set up PYTHONPATH"
export PYTHONPATH=$PYTHONPATH:/usr/lib/python3/dist-packages/:/usr/local/lib/python3/dist-packages:$PWD

echo "Download logni (python lib)"
wget -O - https://raw.githubusercontent.com/erikni/logni.py/develop/setup.sh | bash
echo
