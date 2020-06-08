import paho.mqtt.client as paho
import new_code.crd.credential as data


class Broker:
    def __init__(self):
        self.data = data
        self.client = paho.Client()

    def on_message(self, mosq, obj, msg):
        # converting byte encoded data of message to string format
        payload = msg.payload.decode("utf-8")

    def on_publish(self, mosq, obj, mid):
        mosq.publish(mosq, obj, 0)

    def connect(self):
        """
        connect to mqtt broker
        :return: None
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
        self.client.connect(self.data["portAndIP"]["ip"], self.data["portAndIP"]["port"], 60)

    def subscribe_topics(self):
        """
        Subscribes to multiple topics of smart dustbin.
        :return: on_message function
        """
        self.client.subscribe("test", 0)

    def publish_on_topics(self):
        """
        Publish to dustbin topics
        :return: on_publish function
        """
        self.client.publish('test', '1', 0)
