#!/usr/bin/python2.7
import os, sys

# magia:
proj_path = "/github/pandorabox/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandorabox.settings")
sys.path.append(proj_path)

os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#### script desde aqui:
from ceamon.models import sapnode
from locker.models import *

#todos los abap
#nod = sapnode.objects.filter(product='abap').order_by('sid').values().distinct()
#print nod

#todos los java
#nod = sapnode.objects.filter(product='java').order_by('sid').values().distinct()
#print nod

#todos los webdispatcher
#nod = sapnode.objects.filter(product='webdispatcher').order_by('sid').values().distinct()
#print nod

     #usanmos la tabla status# #fk#    #valor en otra tabla#    #filtro#
#nod = status.objects.filter(sapnode_id__sid='DE0').order_by('sapnode_id').values().distinct()
#print nod

#e = sapnode.objects.get(id=id)
#nod = e.command.all().filter().order_by().values()
#print nod[0]

import requests

p = locker.objects.all()
for x in p: #dentro del obj:
    print(x.e_username)
    print(x.username)

    print(x.e_password)
    print(x.password)

    print(x.e_url)
    print(x.url)

    print(x.e_notes)
    print(x.notes)

