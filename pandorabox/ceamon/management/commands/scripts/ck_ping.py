#!/usr/bin/python2.7
import sys, os, subprocess, traceback, time
from ck_timeout import timeout

name_script = os.path.basename(__file__)

for arg in sys.argv:
    HOST = sys.argv[1]
    SID = sys.argv[2]
    PRODUCT = sys.argv[3]
    pass

#### Variables:
USER="shieren"

COMMANDS = '''
ping -c 1 localhost
'''

ssh = subprocess.Popen(["ssh", USER + "@" + '%s' % HOST, COMMANDS],
                shell=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
res = ssh.stdout.readlines()

SYSTEM = res

def f(*names):
    r = {}
    for n in names:
        r[[ name for name in globals() if globals()[name] is n ][0]] = n
    return r

@timeout(5)
def start_command():
    try:
        if res:
            print f(SYSTEM)
        if not res:
            print("NO DATA?")

    except Exception, err:
        print(traceback.format_exc())

start_command()

