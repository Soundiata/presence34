# This file is executed on every boot (including wake-boot from deepsleep)
import os
from machine import Pin

# constant
PIN_LED = 12
PIN_PIR = 13
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
mqtt_client.connect()

led=Pin(PIN_LED,Pin.OUT)
pir=Pin(PIN_PIR,Pin.IN)
mqtt_message = TOPIC + '/' + str(BOOTH_ID)



def update_presence():
    previous_state = DOWN
    
    while True:
        if (pir.value() == UP) and (previous_state == DOWN):
            led.value(UP)
            mqtt_client.publish(mqtt_message, STATE_USED)
            previous_state = UP
        if (pir.value() == DOWN) and (previous_state == UP):
            led.value(DOWN)
            mqtt_client.publish(mqtt_message, STATE_FREE)
            previous_state = DOWN

update_presence()