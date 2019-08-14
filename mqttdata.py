import paho.mqtt.client as paho
import credential as data
##import RPi.GPIO as GPIO
import serial
import time,sys

def cellular_message(msg_topic):
    if msg.topic=="container1DataGreen" or msg.topic=="container1DataBlue":
        msg="dustbin 1 is full"
    if msg.topic=="container2DataGreen" or msg.topic=="container2DataBlue":
        msg="dustbin 2 is full"
    if msg.topic=="container3DataGreen" or msg.topic=="container3DataBlue":
        msg="dustbin 3 is full"
    if msg.topic=="container4DataGreen" or msg.topic=="container4DataBlue":
        msg="dustbin 2 is full"
    if msg.topic=="container5DataGreen" or msg.topic=="container5DataBlue":
        msg="dustbin 5 is full"
    
    ser.write("AT+CMGF=1\r".encode())
    print("TEXT MODE ENABLED")
    time.sleep(3)
    ser.write('AT+CMGS="**********"\r'.encode())

    time.sleep(3)
    ser.write((msg+chr(26)).encode())
    time.sleep(3)
    print("message sent..")
def on_message(mosq, obj, msg):
    payload=str(msg.payload)

    #dustbin1 data posting
    if msg.topic=="container1DataGreen":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_1_Green","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()
    if msg.topic=="container1DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_1_Blue","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin2 data posting
    if msg.topic=="container2DataGreen":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_2_Green","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()
    if msg.topic=="container2DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_2_Blue","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin3 data posting
    if msg.topic=="container3DataGreen":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_3_Green","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()
    if msg.topic=="container3DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_4_Blue","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin4 data posting
    if msg.topic == "container4DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_4_Green", "w")
        print(msg.topic + payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic=="container4DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_4_Blue","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin5 data posting
    if msg.topic == "container5DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_5_Green", "w")
        print(msg.topic + payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic=="container5DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_5_Blue","w")
        print(msg.topic+payload[2:(len(payload)-1)],file=fp)
        fp.close()
    mosq.publish('pong', 'ack1', 0)
   

def on_publish(mosq, obj, mid):
    pass


if __name__ == '__main__':
    SERIAL_PORT="/dev/ttyS0"
    ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

    data=data.data()
    client = paho.Client()
    
    client.on_message = on_message
    client.on_publish = on_publish
    
    client.username_pw_set(data["user"], data["pw"])
    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect(data["ip"], data["port"], 60)

    client.subscribe("container1DataGreen", 0)
    client.subscribe("container1DataBlue", 0)
    
    #client.publish('reverse', 'ack', 0)
    
    while 1:
        client.loop()
