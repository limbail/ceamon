from tornado.ioloop import PeriodicCallback
from swampdragon.pubsub_providers.data_publisher import publish_data
import psutil
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

    publish_data('sysinfo', {
        'danger_count':danger_count,
        'warning_count': warning_count,
        'instancias_count': instancias_count,
    })
