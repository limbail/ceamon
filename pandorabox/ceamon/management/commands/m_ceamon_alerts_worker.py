#!/usr/bin/python2.7
import os, time, sys, re, inspect, traceback, time, subprocess, json, requests
from threading import Thread
from subprocess import Popen, PIPE
import multiprocessing as mp
from multiprocessing import Pool

# magia:
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
proj_path = "/github/pandorabox/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandorabox.settings")
sys.path.append(proj_path)

os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Importamos Django modules
from django.core.management.base import BaseCommand, CommandError
from ceamon.models import sapnode, CommandModel
from django.core import serializers
from django.db import connection, transaction
#from .scripts.ck_timeout import timeout
from requests.auth import HTTPBasicAuth

ruta_scripts = "/commands/scripts/"

""" # TEMPORAL
from django.contrib.auth.models import User
user = User.objects.create_user(username='service',
                                 email='none@none.com',
                                 password='initial')
"""

username = "service"
password = "initial"
url = "http://localhost:9988/sapnode/"

def get_script_dir(follow_symlinks=True):
    if getattr(sys, False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

def worker(host,active_moni,sid,product,id):
    try:
        if active_moni == "Yes":
            e = sapnode.objects.get(id=id)
            project = e.project.all().filter().order_by().values()
            nod = e.command.all().filter().order_by().values()
            for command in nod:
                command=command['check']
                result = subprocess.Popen(BASE_DIR + ruta_scripts + command + ' ' + host + ' ' + sid + ' ' + product, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                update = result.communicate()[0] # primer item de la lista
                update = str(update) # convertimos a str
                update=update.strip()
                del_simbolo = [ "['" , "']" ] # No funciona con simbolos especiales
                update = update.translate(None, ''.join(del_simbolo)) # el join
                update = update.replace("\\n", "") # simbolo especial x nada
                if command == "ck_os_version.py":
                    print(" Procesing in"+ ' ' + sid + ' ' + "in" + ' ' +  host)
                    print(" El script ha leido ck_os_version.py, y la salida es: ")
                    print update
                    requests.put(url + str(id) + "/", json={'os': update}, auth=HTTPBasicAuth(username, password))
                if command == "ck_ping.py":
                    print(" Procesing in"+ ' ' + sid + ' ' + "in" + ' ' +  host)
                    print(" El script ha leido ck_os_version.py, y la salida es: ")
                    print update
                    requests.put(url + str(id) + "/", json={'os': update}, auth=HTTPBasicAuth(username, password))

        else:
            print(" Monitoring is disabled for"+ ' ' + sid + ' ' + "in" + ' ' +  host)

    except KeyboardInterrupt:
        print "Caught KeyboardInterrupt, terminating workers"
        pool.terminate()
        pool.join()

def handler():
    machines = sapnode.objects.filter().order_by().values()
    pool = mp.Pool(4) # numero maximo de procesos creados por el script
    for x in machines:
        sid=x['sid']
        id=x['id']
        host=x['hostname']
        product=x['product']
        active_moni=x['active_moni'] # (No=desactivado), (Yes=activado)
        pool.apply_async(worker, args=(host,active_moni,sid,product,id,)) # Ejecucion asyncrona de los hosts y ejecucion del worker con argumentos
    pool.close()
    pool.join()

if __name__ == '__main__':
    handler()


