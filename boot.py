#!/usr/bin/python3
# This file is executed on every boot (including wake-boot from deepsleep)
import esp, webrepl, time, network,os

TIMEOUT = 15


# credentials
cred_file = open ('credentials.txt','r')
credentials = cred_file.read()
cred = credentials.split(',')
cred_file.close()

ESSID = cred[0]
PASSWORD = cred[1]


print('Network Connect:',time.localtime())
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ESSID,PASSWORD)
time.sleep(0.1)
for x in range(TIMEOUT):
    if wlan.isconnected():
        break
    time.sleep(1)

# initiate basic services
esp.osdebug(None)
webrepl.start()

def cat(fname):
    f = open(fname, 'r')
    r = f.read()
    f.close()
    print(r)
