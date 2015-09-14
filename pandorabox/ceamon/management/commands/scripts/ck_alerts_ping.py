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
uname -a
'''

def fres():
    try:
        ssh = subprocess.Popen(["ssh", USER + "@" + '%s' % HOST, COMMANDS],
                shell=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        res = ssh.stdout.readlines()
        return res
    except Exception, err:
        print("CONNECTION PROBLEM")

SYSTEM = HOST
STATUS_ID = os.path.basename(__file__)
MODIFIED = "DATE"
# STATUS
if fres():
    STATUS = "DANGER"
else:
    STATUS = "N/A"
# COMMENT
if fres():
    COMMENT = str("Check OK")
else:
    COMMENT = "FAIL"

def f(*names):
    r = {}
    for n in names:
        r[[ name for name in globals() if globals()[name] is n ][0]] = n
    for x in r:
        x = "'" + x + "'"
    return r

@timeout(5)
def start_command():
    try:
        if fres:
            print f(SYSTEM, STATUS_ID, STATUS, COMMENT, MODIFIED)
        if not fres:
           print("NO DATA?")

    except Exception, err:
        print(traceback.format_exc())

start_command()
