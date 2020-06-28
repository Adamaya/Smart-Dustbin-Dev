import paho.mqtt.client as paho
import new_code.crd.credential as data
import new_code.dump.methods.features as features


class Broker:
    def __init__(self):
        self.data = data
        self.client = paho.Client()
        self.node_ping = "0"

    def on_message(self, mosq, obj, msg):
        """
        this function is called by subscribe function. In this function we are fetching the message from the subscribed
        channel and decoding it into string format. After that auto_adjust function is called to adjust the payload
        value according to dustbin capacity and storing it into adjust_value. After that we are posting data on the
        dynamo db.

        :param msg: message of MQTT
        :return: null
        """
        # converting byte encoded data of message to string format
        payload = msg.payload.decode("utf-8")
        if msg.topic in ["container1Data", "container2Data", "container3Data", "container4Data"]:
            adjusted_value = features.auto_adjust(payload, msg.topic)
            features.update_dynamo_db(adjusted_value, msg.topic)
            features.upload_to_s3(msg.topic)
            self.node_ping = "1"

    def on_publish(self, mosq, obj, mid):
        mosq.publish(mosq, obj, 0)

    def connect(self):
        """
        connect to mqtt broker
        :return: null
        """
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

        # setting users(dustbins)
        self.client.username_pw_set(self.data.users["user1"], self.data.passwd["user1"])
        self.client.username_pw_set(self.data.users["user2"], self.data.passwd["user2"])
        self.client.username_pw_set(self.data.users["user3"], self.data.passwd["user3"])
        self.client.username_pw_set(self.data.users["user4"], self.data.passwd["user4"])
        self.client.username_pw_set(self.data.users["user5"], self.data.passwd["user5"])

        # connecting to mqtt broker
        self.client.connect(self.data.portAndIP["ip"], self.data.portAndIP["port"], 60)

    def subscribe_topics(self):
        """
        Subscribes to multiple topics of smart dustbin.
        :return: on_message function
        """
        self.client.subscribe("container1Data", 0)
        self.client.subscribe("container2Data", 0)
        self.client.subscribe("container3Data", 0)
        self.client.subscribe("container4Data", 0)
        self.client.subscribe("container1DataPing", 0)
        self.client.subscribe("container2DataPing", 0)
        self.client.subscribe("container3DataPing", 0)
        self.client.subscribe("container4DataPing", 0)

    def publish_on_topics(self, topic):
        """
        Publish to dustbin topics
        :return: on_publish function
        """
        self.client.publish(topic, '1', 0)
