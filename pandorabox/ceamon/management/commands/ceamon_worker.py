#!/usr/bin/env python
# Python modules
import os, sys, re, inspect, traceback, time, subprocess, json, requests
from threading import Thread
from subprocess import Popen, PIPE
# Importamos Django modules
from django.core.management.base import BaseCommand, CommandError
from ceamon.models import sapnode, CommandModel
from django.core import serializers
from django.db import connection, transaction
from .scripts.ck_timeout import timeout
from requests.auth import HTTPBasicAuth

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ruta_scripts = "/scripts/"

# magia nivel 80:
proj_path = os.path.join(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandorabox.settings")
sys.path.append(proj_path)

os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#### script desde aqui:

# Definimos globales
username = "test01"
password = "1234?"
url = "http://localhost:9988/sapnode/"
#id = "1"
#requests.put(url + id + "/", json={'os': 'prueba'})


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

class Command(BaseCommand):
    args = 'Por ahora no se necesitan argumentos'
    help = 'Ceamon serial killer'

    def handle(self, *args, **options):
        try:
            machines = sapnode.objects.filter().order_by().values()
            for x in machines: 
                sid=x['sid']
                id=x['id']
                hostname=x['hostname']
                product=x['product']
                active_moni=x['active_moni'] # (0=desactivado), (1=activado)
		print active_moni

		e = sapnode.objects.get(id=id)
		nod = e.command.all().filter().order_by().values()

                if active_moni == "Yes":
                    for command in nod:
                        command=command['status']
                        #if command:
                            #print command
                            #print hostname
	         	    #print hostname
		            #print command
                        result = subprocess.Popen(get_script_dir() + ruta_scripts + command + ' ' + hostname + ' ' + sid + ' ' + product, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

                        update = result.communicate()[0] # primer item de la lista
                        update = str(update) # convertimos a str
                        update=update.strip()
                        del_simbolo = [ "['" , "']" ] # No funciona con simbolos especiales
                        update = update.translate(None, ''.join(del_simbolo)) # el join
                        update = update.replace("\\n", "") # simbolo especial x nada

                        if command == "ck_os_version.py": # Dependiendo del argumento pasado leemos su salida
                            print id
                            print("El script ha leido ck_os_version.py, y la salida es: ")
                            print update
                            #p = sapnode.objects.get(pk=id) # Eliminamos la actualizacion por objeto
                            #p.os = update 
                            #p.save()

                            requests.put(url + str(id) + "/", json={'os': update}, auth=HTTPBasicAuth(username, password)) # Ahora actualilzamos al JSON

                        elif command == "ck_db_version.py":
                            print("El script ha leido ck_db_version.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'database': update}, auth=HTTPBasicAuth(username, password))

                        elif command == "ck_dbv_version.py":
                            print("El script ha leido ck_dbv_version.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'database_v': update}, auth=HTTPBasicAuth(username, password))

                        elif command == "ck_gettotalsizefs.py":
                            print("El script ha leido ck_gettotalsizefs.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'asi_disk': update}, auth=HTTPBasicAuth(username, password))

                        elif command == "ck_get_num_cpus.py":
                            print("El script ha leido ck_get_num_cpus.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'cpu': update}, auth=HTTPBasicAuth(username, password))

                        elif command == "ck_osv_version.py":
                            print("El script ha leido ck_osv_version.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'os_v': update}, auth=HTTPBasicAuth(username, password))

                        elif command == "ck_get_ram.py":
                            print("El script ha leido ck_get_ram.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'asi_ram': update}, auth=HTTPBasicAuth(username, password))

                        elif command == "ck_sap_kernel_version.py":
                            print("El script ha leido ck_sap_kernel_version.py, y la salida es: ")
                            print update

                            requests.put(url + str(id) + "/", json={'sap_kernel': update}, auth=HTTPBasicAuth(username, password))

                else:
                    print("Monitoring is disabled for"+ ' ' + sid + ' ' + "in" + ' ' +  hostname)
        
                print('-')*80
                print('-')*80

        
            return

	except Exception, err:
            print(traceback.format_exc())

