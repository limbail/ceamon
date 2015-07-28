#!/usr/bin/env python
import sys, os, subprocess, traceback, time
from ck_timeout import timeout

name_script = os.path.basename(__file__)

for arg in sys.argv:
    HOST = sys.argv[1]
    SID = sys.argv[2]
    PRODUCT = sys.argv[3]
    pass

#### Variables:
USER = (SID.lower()) + "adm"

COMMANDS = '''
df -h -P | awk -F ' ' '{print $2}' | grep G | grep -iv size | sed 's/G$//' | paste -sd+ - | bc
'''

@timeout(5)
def start_command():

    try:
        ssh = subprocess.Popen(["ssh", USER + "@" + '%s' % HOST, COMMANDS],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        res = ssh.stdout.readlines()

        if res:
            print str(res)
        if not res:
            print("NO DATA?")

    except Exception, err:
        print(traceback.format_exc())

start_command()

