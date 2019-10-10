import paho.mqtt.client as paho
import datetime
import credential as data
import RPi.GPIO as GPIO
import serial
import time, sys


# TODO change the path
# TODO change ultrasonic value according to dustbin height

def cellular_message(msg_topic):
    if msg_topic == "container1DataGreen" or msg_topic == "container1DataBlue":
        message = "dustbin 1 is full"
    if msg_topic == "container2DataGreen" or msg_topic == "container2DataBlue":
        message = "dustbin 2 is full"
    if msg_topic == "container3DataGreen" or msg_topic == "container3DataBlue":
        message = "dustbin 3 is full"
    if msg_topic == "container4DataGreen" or msg_topic == "container4DataBlue":
        message = "dustbin 2 is full"
    if msg_topic == "container5DataGreen" or msg_topic == "container5DataBlue":
        message = "dustbin 5 is full"

    ser.write("AT+CMGF=1\r".encode())
    print("TEXT MODE ENABLED")
    time.sleep(3)
    ser.write('AT+CMGS="**********"\r'.encode())

    time.sleep(3)
    ser.write((message + chr(26)).encode())
    time.sleep(3)
    print("message sent..")


def on_message(mosq, obj, msg):
    payload = str(msg.payload)

    # Send message
    if (int(payload[2:(len(payload) - 1)])) > 80:
        cellular_message(msg.topic)

    # dustbin1 data posting
    if msg.topic == "container1DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_1_Green.json", "w")
        if 76 < (int(payload[2:(len(payload) - 1)])):
            print("0", file=fp)
        elif 72 < (int(payload[2:(len(payload) - 1)])) <= 76:
            print("5", file=fp)
        elif 68 < (int(payload[2:(len(payload) - 1)])) <= 72:
            print("10", file=fp)
        elif 64 < (int(payload[2:(len(payload) - 1)])) <= 68:
            print("15", file=fp)
        elif 60 < (int(payload[2:(len(payload) - 1)])) <= 64:
            print("20", file=fp)
        elif 56 < (int(payload[2:(len(payload) - 1)])) <= 60:
            print("25", file=fp)
        elif 52 < (int(payload[2:(len(payload) - 1)])) <= 56:
            print("30", file=fp)
        elif 48 < (int(payload[2:(len(payload) - 1)])) <= 52:
            print("35", file=fp)
        elif 44 < (int(payload[2:(len(payload) - 1)])) <= 48:
            print("40", file=fp)
        elif 40 < (int(payload[2:(len(payload) - 1)])) <= 44:
            print("45", file=fp)
        elif 36 < (int(payload[2:(len(payload) - 1)])) <= 40:
            print("50", file=fp)
        elif 32 < (int(payload[2:(len(payload) - 1)])) <= 36:
            print("55", file=fp)
        elif 28 < (int(payload[2:(len(payload) - 1)])) <= 32:
            print("60", file=fp)
        elif 24 < (int(payload[2:(len(payload) - 1)])) <= 28:
            print("65", file=fp)
        elif 20 < (int(payload[2:(len(payload) - 1)])) <= 24:
            print("70", file=fp)
        elif 16 < (int(payload[2:(len(payload) - 1)])) <= 20:
            print("75", file=fp)
        elif 12 < (int(payload[2:(len(payload) - 1)])) <= 16:
            print("80", file=fp)
        elif 8 < (int(payload[2:(len(payload) - 1)])) <= 12:
            print("85", file=fp)
        elif 4 < (int(payload[2:(len(payload) - 1)])) <= 8:
            print("90", file=fp)
        elif 0 < (int(payload[2:(len(payload) - 1)])) <= 4:
            print("100", file=fp)
        else:
            print("Invalid Value", file=fp)
        fp.close()
    if msg.topic == "container1DataBlue":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_1_Blue.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()

    # dustbin2 data posting
    if msg.topic == "container2DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_2_Green.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic == "container2DataBlue":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_2_Blue.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()

    # dustbin3 data posting
    if msg.topic == "container3DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_3_Green.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic == "container3DataBlue":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_4_Blue.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()

    # dustbin4 data posting
    if msg.topic == "container4DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_4_Green.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic == "container4DataBlue":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_4_Blue.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()

    # dustbin5 data posting
    if msg.topic == "container5DataGreen":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_5_Green.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    if msg.topic == "container5DataBlue":
        fp = open("C:\Apache24\htdocs\Data\Dustbin_5_Blue.json", "w")
        print(payload[2:(len(payload) - 1)], file=fp)
        fp.close()
    mosq.publish('pong', 'ack1', 0)


def on_publish(mosq, obj, mid):
    pass


if __name__ == '__main__':
    SERIAL_PORT = "/dev/ttyS0"
    ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=5)

    data = data.data()  # my credential
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

    # client.publish('reverse', 'ack', 0)

    while 1:
        client.loop()
