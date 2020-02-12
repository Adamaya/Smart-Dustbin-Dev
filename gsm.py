import time
import serial

recipient = "+1234567890"
message = "Hello, World!"

phone = serial.Serial("/dev/ttyACM0",  460800, timeout=5)
try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    phone.write(bytes([26]))
    time.sleep(0.5)
else:
    print("not connected")
finally:
    phone.close()
