#!/usr/bin/bash
screen -d -m -S "ceamon" bash -c 'cd /github/pandorabox/ && /usr/bin/python2.7 /github/pandorabox/manage.py runserver 0.0.0.0:9988'
screen -d -m -S "realtime" bash -c 'cd /github/pandorabox/ && /usr/bin/python2.7 /github/pandorabox/server.py'
