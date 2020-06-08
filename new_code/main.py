import base64
import new_code.broker.mqtt_connection
import paho.mqtt.client as paho
import new_code.crd.credential as data
from time import sleep
import datetime

import new_code.dump.methods.crd as credential

print()
string = base64.b64encode(base64.b64encode(b"hello"))
print(string.decode("utf-8"))

# broker=new_code.broker.mqtt_connection.Broker()
# broker.connect()
# broker.subscribe_topics()
# while 1:
#     broker.client.loop()
