import paho.mqtt.client as paho
import credential as data
import RPi.GPIO as GPIO
import serial
import time, sys


# TODO change the path
# TODO change ultrasonic value according to dustbin height
# TODO CHANGE THE IP ADDRESS ACCORDING TO YOUR MQTT BROKER

def cellular_message(msg_topic):
    dustbins = {"container1Data": "Dustbin 1",
                "container2Data": "Dustbin 2",
                "container3Data": "Dustbin 3",
                "container4Data": "Dustbin 4",
                "container5Data": "Dustbin 5",
                }

    ser.write("AT+CMGF=1\r".encode())
    print("TEXT MODE ENABLED")
    time.sleep(3)
    ser.write('AT+CMGS="**********"\r'.encode())

    time.sleep(3)
    ser.write((dustbins[msg_topic] + chr(26)).encode())
    time.sleep(3)
    print("message sent..")


def on_message(mosq, obj, msg):
    # converting byte encoded data of message to string format
    payload = msg.payload.decode("utf-8")

    # Send message
    if (int(payload) < 20):
        pass
    # cellular_message(msg.topic)
    # defining datafile names of each dustbin published topic where payload gonna be store
    dataFile = {"container1Data": "Dustbin_1_Blue.json",
                "container2Data": "Dustbin_2_Blue.json",
                "container3Data": "Dustbin_3_Blue.json",
                "container4Data": "Dustbin_4_Blue.json",
                "container5Data": "Dustbin_5_Blue.json"
                }

    fp = open("/var/www/html/Data/" + dataFile[msg.topic], "w")
    if (89 < int(payload)):
        print("0", file=fp)
        print("0%")
    elif 84 < int(payload) <= 88:
        print("5", file=fp)
        print("5%")
    elif 80 < int(payload) <= 84:
        print("10", file=fp)
        print("10%")
    elif 76 < int(payload) <= 80:
        print("15", file=fp)
        print("15%")
    elif 72 < int(payload) <= 76:
        print("20", file=fp)
        print("20%")
    elif 68 < int(payload) <= 72:
        print("25", file=fp)
        print("25%")
    elif 64 < int(payload) <= 68:
        print("30", file=fp)
        print("30%")
    elif 60 < int(payload) <= 64:
        print("35", file=fp)
        print("35%")
    elif 56 < int(payload) <= 60:
        print("40", file=fp)
        print("40%")
    elif 52 < int(payload) <= 56:
        print("45", file=fp)
        print("45%")
    elif 48 < int(payload) <= 52:
        print("50", file=fp)
        print("50%")
    elif 44 < int(payload) <= 48:
        print("55", file=fp)
        print("55%")
    elif 40 < int(payload) <= 44:
        print("60", file=fp)
        print("60%")
    elif 36 < int(payload) <= 40:
        print("65", file=fp)
        print("65%")
    elif 32 < int(payload) <= 36:
        print("70", file=fp)
        print("70%")
    elif 28 < int(payload) <= 32:
        print("75", file=fp)
        print("75%")
    elif 24 < int(payload) <= 28:
        print("80", file=fp)
        print("80%")
    elif 20 < int(payload) <= 24:
        print("85", file=fp)
        print("85%")
    elif 16 < int(payload) <= 20:
        print("90", file=fp)
        print("90%")
    elif (int(payload) <= 16):
        print("100", file=fp)
        print("100%")

    else:
        print("Invalid Value" + int(payload), file=fp)
    fp.close()

    mosq.publish('pong', 'ack1', 0)


def on_publish(mosq, obj, mid):
    pass


if __name__ == '__main__':
    # SERIAL_PORT = "/dev/ttyS0"
    # ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=5)

    data = data.data()  # my credential
    client = paho.Client()

    client.on_message = on_message
    client.on_publish = on_publish

    # setting users(dustbins)
    client.username_pw_set(data["user1"], data["pw"])
    client.username_pw_set(data["user2"], data["pw"])
    client.username_pw_set(data["user3"], data["pw"])
    client.username_pw_set(data["user4"], data["pw"])
    client.username_pw_set(data["user5"], data["pw"])

    # connecting to mqtt broker
    client.connect(data["ip"], data["port"], 60)

    # subscribing the topics which are published by dustbins
    client.subscribe("container1Data", 0)
    client.subscribe("container2Data", 0)
    client.subscribe("container3Data", 0)
    client.subscribe("container4Data", 0)
    client.subscribe("container5Data", 0)
    client.publish('dustbinNo', '1', 0)
    client.publish('dustbinNo', '2', 0)
    client.publish('dustbinNo', '3', 0)
    client.publish('dustbinNo', '4', 0)
    client.publish('dustbinNo', '5', 0)

    while 1:
        client.loop()
