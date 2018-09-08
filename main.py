# This file is executed on every boot (including wake-boot from deepsleep)
import nettools
from machine import Pin

# constant
PIN_LED = 15
PIN_PIR = 12
BOOTH_ID = 1234
TOPIC = 'presence34'
UP = 1
DOWN = 0
STATE_USED = 'USED'
STATE_FREE = 'FREE'
MQTT_CLIENTID = "Client-DZFREZG54VDF24F2B-" + str(BOOTH_ID)
MQTT_BROKER = 'test.mosquitto.org'

# credentials
cred_file = open ('credentials.txt','r')
credentials = cred_file.read()
cred = credentials.split(',')
ESSID = cred[0]
PASSWORD = cred[1]


nettools.wlan_connect(ESSID, PASSWORD)

nettools.initiate_mqtt()
mqtt_client = MQTTClient(MQTT_CLIENTID, MQTT_BROKER)


led=Pin(PIN_LED,Pin.OUT)
pir=Pin(PIN_PIR,Pin.IN)
mqtt_message = TOPIC + '/' + str(BOOTH_ID)


def update_presence():
    while True:
        if pir.value() == 1:
            led.value(1)
            mqtt_client.publish(mqtt_message, STATE_USED)
        if pir.value() == 0:
            led.value()
            mqtt_client.publish(mqtt_message, STATE_FREE)