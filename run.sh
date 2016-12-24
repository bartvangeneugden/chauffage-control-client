#/bin/sh
git pull origin master
curl http://localhost:3000/api > config.json
python control.py