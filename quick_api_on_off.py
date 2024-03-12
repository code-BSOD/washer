from bottle import run, get
import sys
import random
from paho.mqtt import client as mqtt_client


client_id = f'python_mqtt_-{random.randint(0, 1000)}'

# client = mqtt_client.Client(client_id)
client = mqtt_client.Client(client_id)

@get('/on')
def power_on():
    if client.connect('131.159.6.111', 1883, 60) != 0:
        print("Could NOT connect to broker")
        return {'success': False}

    topic = "cmnd/washer/Power"

    client.publish(topic, 'on', 0)

    client.disconnect()

    return {'success': True}



@get('/off')
def power_on():
    if client.connect('131.159.6.111', 1883, 60) != 0:
        print("Could NOT connect to broker")
        return {'success': False}

    topic = "cmnd/washer/Power"

    client.publish(topic, 'off', 0)

    client.disconnect()

    return {'success': True}

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, reloader=True)
