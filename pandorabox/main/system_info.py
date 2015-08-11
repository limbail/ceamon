from tornado.ioloop import PeriodicCallback
from swampdragon.pubsub_providers.data_publisher import publish_data
import requests, json
from ceamon.models import sapnode

url = "http://localhost:9988/sapnode/"

pcb = None

def broadcast_sys_info():
    global pcb

    if pcb is None:
        pcb = PeriodicCallback(broadcast_sys_info, 3000)
        pcb.start()

    danger = sapnode.objects.filter(status='danger').order_by('sid').values().distinct()
    danger_count=len(danger)

    warning = sapnode.objects.filter(status='warning').order_by('sid').values().distinct()
    warning_count=len(warning)

    instancias = sapnode.objects.filter().order_by('sid').values().distinct()
    instancias_count=len(instancias)

    instancias_abap = sapnode.objects.filter(product='abap').order_by('sid').values().distinct()
    instancias_abap_count=len(instancias_abap)

    instancias_portal = sapnode.objects.filter(product='portal').order_by('sid').values().distinct()
    instancias_portal_count=len(instancias_portal)

    instancias_javaengine = sapnode.objects.filter(product='java_engine').order_by('sid').values().distinct()
    instancias_javaengine_count=len(instancias_javaengine)

    instancias_opentext = sapnode.objects.filter(product='opentext').order_by('sid').values().distinct()
    instancias_opentext_count=len(instancias_opentext)

    publish_data('sysinfo', {
        'danger_count':danger_count,
        'warning_count': warning_count,
        'instancias_count': instancias_count,
        'instancias_abap_count':instancias_abap_count,
        'instancias_portal_count':instancias_portal_count,
        'instancias_javaengine_count':instancias_javaengine_count,
        'instancias_opentext_count':instancias_opentext_count,

    })
