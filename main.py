# This file is executed on every boot (including wake-boot from deepsleep)
import os
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

if 'umqtt' not in os.listdir('/lib'):
    import upip
    upip.install('micropython-umqtt.robust')
    upip.install('micropython-umqtt.simple')
from umqtt.simple import MQTTClient

mqtt_client = MQTTClient(MQTT_CLIENTID, MQTT_BROKER)


led=Pin(PIN_LED,Pin.OUT)
pir=Pin(PIN_PIR,Pin.IN)
mqtt_message = TOPIC + '/' + str(BOOTH_ID)


def update_presence():
    while True:
        if pir.value() == UP:
            led.value(UP)
            mqtt_client.publish(mqtt_message, STATE_USED)
        if pir.value() == DOWN:
            led.value(DOWN)
            mqtt_client.publish(mqtt_message, STATE_FREE)