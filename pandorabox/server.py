#!/usr/bin/python2.7
import os
import sys


from swampdragon.swampdragon_server import run_server

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandorabox.settings")

host_port = sys.argv[1] if len(sys.argv) > 1 else None

run_server(host_port=host_port)

