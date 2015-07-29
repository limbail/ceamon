#!/usr/bin/python2.7
import os, time, sys, re, inspect, traceback, time, subprocess, json, requests
from requests.auth import HTTPBasicAuth

username = "service"
password = "initial"
url = "http://localhost:9988/sapnode/"
update = "LINUXa"

r = requests.put(url + str(1) + "/", json={'os_v': update}, auth=HTTPBasicAuth(username,password))
#r = requests.get(url + str(1) + "/", auth=('username', 'password'))
print r.text
