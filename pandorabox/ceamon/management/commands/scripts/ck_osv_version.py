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
cat /etc/redhat-release | awk -F ' ' '{print $1 $2 $7 $8}'
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
            print res
        if not res:
            print("NO DATA?")

    except Exception, err:
        print(traceback.format_exc())

start_command()

