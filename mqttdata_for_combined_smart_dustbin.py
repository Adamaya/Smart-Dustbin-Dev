import paho.mqtt.client as paho
import datetime
import credential as data
import RPi.GPIO as GPIO
import serial
import time, sys


# TODO change the path
# TODO change ultrasonic value according to dustbin height

def cellular_message(msg_topic):
    dustbins = {"container1DataGreen": "Dustbin 1", "container1DataBlue": "Dustbin 1",
                "container2DataGreen": "Dustbin 2", "container2DataBlue": "Dustbin 2",
                "container3DataGreen": "Dustbin 3", "container3DataBlue": "Dustbin 3",
                "container4DataGreen": "Dustbin 4", "container4DataBlue": "Dustbin 4",
                "container5DataGreen": "Dustbin 5", "container5DataBlue": "Dustbin 5",
                }

    ser.write("AT+CMGF=1\r".encode())
    print("TEXT MODE ENABLED")
    time.sleep(3)
    ser.write('AT+CMGS="9045328260"\r'.encode())

    time.sleep(3)
    ser.write((dustbins[msg_topic] + chr(26)).encode())
    time.sleep(3)
    print("message sent..")


def on_message(mosq, obj, msg):
    payload = str(msg.payload)

    # Send message
    if (int(payload[2:(len(payload) - 1)])) < 20:
        cellular_message(msg.topic)
    dataFile = {"container1DataGreen": "Dustbin_1_Green.json", "container1DataBlue": "Dustbin_1_Blue.json",
                "container2DataGreen": "Dustbin_2_Green.json", "container2DataBlue": "Dustbin_2_Blue.json",
                "container3DataGreen": "Dustbin_3_Green.json", "container3DataBlue": "Dustbin_3_Blue.json",
                "container4DataGreen": "Dustbin_4_Green.json", "container4DataBlue": "Dustbin_4_Blue.json",
                "container5DataGreen": "Dustbin_5_Green.json", "container5DataBlue": "Dustbin_5_Blue.json",
                }
    # dustbin data posting

    fp = open("C:\Apache24\htdocs\Data\\" + dataFile[msg.topic], "w")
    if 89 < (int(payload[2:(len(payload) - 2)])):
        print("0", file=fp)
    elif 84 < (int(payload[2:(len(payload) - 2)])) <= 88:
        print("5", file=fp)
    elif 80 < (int(payload[2:(len(payload) - 2)])) <= 84:
        print("10", file=fp)
    elif 76 < (int(payload[2:(len(payload) - 2)])) <= 80:
        print("15", file=fp)
    elif 72 < (int(payload[2:(len(payload) - 2)])) <= 76:
        print("20", file=fp)
    elif 68 < (int(payload[2:(len(payload) - 2)])) <= 72:
        print("25", file=fp)
    elif 64 < (int(payload[2:(len(payload) - 2)])) <= 68:
        print("30", file=fp)
    elif 60 < (int(payload[2:(len(payload) - 2)])) <= 64:
        print("35", file=fp)
    elif 56 < (int(payload[2:(len(payload) - 2)])) <= 60:
        print("40", file=fp)
    elif 52 < (int(payload[2:(len(payload) - 2)])) <= 56:
        print("45", file=fp)
    elif 48 < (int(payload[2:(len(payload) - 2)])) <= 52:
        print("50", file=fp)
    elif 44 < (int(payload[2:(len(payload) - 2)])) <= 48:
        print("55", file=fp)
    elif 40 < (int(payload[2:(len(payload) - 2)])) <= 44:
        print("60", file=fp)
    elif 36 < (int(payload[2:(len(payload) - 2)])) <= 40:
        print("65", file=fp)
    elif 32 < (int(payload[2:(len(payload) - 2)])) <= 36:
        print("70", file=fp)
    elif 28 < (int(payload[2:(len(payload) - 2)])) <= 32:
        print("75", file=fp)
    elif 24 < (int(payload[2:(len(payload) - 2)])) <= 28:
        print("80", file=fp)
    elif 20 < (int(payload[2:(len(payload) - 2)])) <= 24:
        print("85", file=fp)
    elif 16 < (int(payload[2:(len(payload) - 2)])) <= 20:
        print("90", file=fp)
    elif 12 <= (int(payload[2:(len(payload) - 2)])) <= 16:
        print("100", file=fp)
    else:
        print("Invalid Value", file=fp)
    fp.close()


# mosq.publish('pong', 'ack1', 0)


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

    while 1:
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
