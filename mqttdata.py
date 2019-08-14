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

    #Send message
    if(int(payload[2:(len(payload)-1)]))>80:
        cellular_message(msg.topic)
        
    #dustbin1 data posting
    if msg.topic=="container1DataGreen":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_1_Green.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
        fp.close()
    if msg.topic=="container1DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_1_Blue.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin2 data posting
    if msg.topic=="container2DataGreen":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_2_Green.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
        fp.close()
    if msg.topic=="container2DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_2_Blue.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin3 data posting
    if msg.topic=="container3DataGreen":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_3_Green.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
        fp.close()
    if msg.topic=="container3DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_4_Blue.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
        fp.close()

    # dustbin4 data posting
    if msg.topic == "container4DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_4_Green.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic=="container4DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_4_Blue.json","w")
        print(payload[2:(len(payload) -1 )], file=fp)
        fp.close()

    # dustbin5 data posting
    if msg.topic == "container5DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_5_Green.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic=="container5DataBlue":
        fp=open("C:\Apache24\htdocs\Data\Dustbin_5_Blue.json","w")
        print(payload[2:(len(payload)-1)],file=fp)
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
    
    client.username_pw_set(data["user1"], data["pw"])
    client.username_pw_set(data["user2"], data["pw"])
    client.username_pw_set(data["user3"], data["pw"])
    client.username_pw_set(data["user4"], data["pw"])
    client.username_pw_set(data["user5"], data["pw"])
    
    client.connect(data["ip"], data["port"], 60)

    client.subscribe("container1DataGreen", 0)
    client.subscribe("container1DataBlue", 0)
    client.subscribe("container2DataGreen", 0)
    client.subscribe("container2DataBlue", 0)
    client.subscribe("container3DataGreen", 0)
    client.subscribe("container3DataBlue", 0)
    client.subscribe("container4DataGreen", 0)
    client.subscribe("container4DataBlue", 0)
    client.subscribe("container5DataGreen", 0)
    client.subscribe("container5DataBlue", 0)
    
    #client.publish('reverse', 'ack', 0)
    
    while 1:
        client.loop()
