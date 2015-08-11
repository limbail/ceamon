#!/usr/bin/python2.7
import os, time, sys, re, inspect, traceback, time, subprocess, json, requests, urllib
from requests.auth import HTTPBasicAuth

username = "service"
password = "initial"
url = "http://localhost:9988/sapnode/"
update = "LINUX"

#r = requests.put(url + str(1) + "/", json={'os': update}, auth=HTTPBasicAuth(username,password))
#print r.text

url = urllib.urlopen("http://service:initial@localhost:9988/sapnode/")
values = json.load(url)
for x in values:
    for key, value in x.iteritems():
        print key, 'is:', value
    print ''
url.close()
