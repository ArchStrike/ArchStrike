#!/bin/bash
# start whole mosquito toolkit on Arch based systems
cd /usr/share/mosquito
python2 mosquito/start.py 8082 4444 --http 8000
echo "Please open http://localhost:8000/generate.html in your browser"
