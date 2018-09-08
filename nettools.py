#!/usr/bin/python3
# imports
import sys, network, time, os

# kill all on start
network.WLAN(network.STA_IF).active(False)
network.WLAN(network.AP_IF).active(False)

# connect to WiFi LAN
def wlan_connect(essid,password,timeout=15):
    print('Network Connect:',time.localtime())
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(essid,password)
        time.sleep(0.1)
        for x in range(timeout):
            if wlan.isconnected():
                break
            time.sleep(1)
    return_value = wlan.isconnected()
    print('Network Connect:',return_value)
    #print('Network Status:',wlan.status())
    return return_value

# disconnect from wlan
def wlan_disconnect(timeout=15):
    print('Network Disconnect:',time.localtime())
    wlan = network.WLAN(network.STA_IF)
    return_value = True
    if wlan.active():
        if wlan.isconnected():
            wlan.disconnect()
            time.sleep(0.1)
            for x in range(timeout):
                if not wlan.isconnected():
                    break
                time.sleep(1)
            return_value = not wlan.isconnected()
    wlan.active(False)
    print('Network Disonnect:',return_value)
    #print('Network Status:',wlan.status())
    return return_value

def initiate_mqtt():
    if 'mqtt' not in os.listdir('/lib'):
        import upip
        upip.install('micropython-umqtt.robust')
        upip.install('micropython-umqtt.simple')
    
    from mqtt.simple import MQTTClient