import new_code.dump.methods.crd as credential
import datetime, serial, boto3
from time import sleep

# set the 5 percentage value of dustbin.
value = (int(100) * 5) // 100


def auto_adjust(payload, topic):
    """
            converts the input payload into percentage value and update the json file to update the state of dustbin
            :param payload: data received from sensor
            :param topic:  on what topic data is recived
            :return: converted value.
            """
    if value * 19 < int(payload):
        update_json("0", topic)
        print("0%")
        return 0
    elif value * 18 < int(payload) <= value * 19:
        update_json("5", topic)
        print("5%")
        return 5
    elif value * 17 < int(payload) <= value * 18:
        update_json("10", topic)
        print("10%")
        return 10
    elif value * 16 < int(payload) <= value * 17:
        update_json("15", topic)
        print("15%")
        return 15
    elif value * 15 < int(payload) <= value * 16:
        update_json("20", topic)
        print("20%")
        return 20
    elif value * 14 < int(payload) <= value * 15:
        update_json("25", topic)
        print("25%")
        return 25
    elif value * 13 < int(payload) <= value * 14:
        update_json("30", topic)
        print("30%")
        return 30
    elif value * 12 < int(payload) <= value * 13:
        update_json("35", topic)
        print("35%")
        return 35
    elif value * 11 < int(payload) <= value * 12:
        update_json("40", topic)
        print("40%")
        return 40
    elif value * 10 < int(payload) <= value * 11:
        update_json("45", topic)
        print("45%")
        return 45
    elif value * 9 < int(payload) <= value * 10:
        update_json("50", topic)
        print("50%")
        return 50
    elif value * 8 < int(payload) <= value * 9:
        update_json("55", topic)
        print("55%")
        return 55
    elif value * 7 < int(payload) <= value * 8:
        update_json("60", topic)
        print("60%")
        return 60
    elif value * 6 < int(payload) <= value * 7:
        update_json("65", topic)
        print("65%")
        return 65
    elif value * 5 < int(payload) <= value * 6:
        update_json("70", topic)
        print("70%")
        return 70
    elif value * 4 < int(payload) <= value * 5:
        update_json("75", topic)
        print("75%")
        return 75
    elif value * 3 < int(payload) <= value * 4:
        update_json("80", topic)
        print("80%")
        return 80
    elif value * 2 < int(payload) <= value * 3:
        update_json("85", topic)
        print("85%")
        return 85
    elif value * 1 < int(payload) <= value * 2:
        update_json("90", topic)
        print("90%")
        return 90
    elif (int(payload) <= value * 1):
        update_json("100", topic)
        print("100%")
        return 100
    else:
        print("Invalid Value" + payload)


def update_json(payload, topic):
    """
    update the state of the dustbin in JSON file
    :param payload: recieve the converted value
    :param topic: topic on sender
    :return: null
    """
    file_name = credential.json_data_files[topic]
    fp = open("new_code/dump/database/" + file_name, "w")
    print("{\n  filled: " + payload +
          ",\n  last_updated: " + str(datetime.datetime.now()) + " \n}", file=fp)
    fp.close()


def upload_to_s3(topic):
    """
    upload JSON files to s3 bucket on aws cloud
    :param topic: topic of the file
    :return: null
    """
    s3 = boto3.client("s3")
    file_name = 'new_code\\dump\\database\\' + credential.json_data_files[topic]
    bucket = 'smart-dustbins'
    object_name = credential.json_data_files[topic]
    s3.upload_file(file_name, bucket, object_name)


def update_dynamo_db(value, topic):
    """
    send converted sensor value to dynamo db on aws cloud
    :param value: converted sensor value
    :param topic: topic of
    :return: null
    """

    Table_Name = 'Live_Status'
    now = datetime.datetime.now()
    date = now.strftime('%d %B %Y')
    current_time = now.strftime("%H:%M:%S")
    db = boto3.resource('dynamodb')
    table = db.Table(Table_Name)
    table.put_item(
        Item={
            'dustbin_id': str(credential.dynamo_db_table[topic]),
            'date': date,
            'time': str(current_time),
            'location_name': "AB1",
            'latitude': str(25.69),
            'longditude': str(69.56),
            'sweeper_contact_no': str("+91xxxxxxxxxx"),
            'sweeper_name': 'demo',
            'sensor_value': str(value)
        }
    )


def sms_service():
    """
    sends sms to sweeper of area.
    :return: null
    """
    recipient = "+1234567890"
    message = "Hello, World!"

    phone = serial.Serial("/dev/ttyACM0", 460800, timeout=5)
    try:
        sleep(0.5)
        phone.write(b'ATZ\r')
        sleep(0.5)
        phone.write(b'AT+CMGF=1\r')
        sleep(0.5)
        phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        sleep(0.5)
        phone.write(message.encode() + b"\r")
        sleep(0.5)
        phone.write(bytes([26]))
        sleep(0.5)
    except Exception as e:
        print("not connected")
    finally:
        phone.close()
