import new_code.broker.mqtt_connection

broker = new_code.broker.mqtt_connection.Broker()
broker.connect()
broker.subscribe_topics()
dustbin_no = 0
ping = 0

while 1:

    broker.client.loop()

    if dustbin_no % 4 == 0:
        if ping == 0:
            broker.publish_on_topics("container1Ping")
            ping = 1
        if broker.node_ping != "1":
            continue
        ping = 0
        dustbin_no = dustbin_no + 1
        broker.node_ping = "0"

    elif dustbin_no % 4 == 1:
        if ping == 0:
            broker.publish_on_topics("container2Ping")
            ping = 1
        if broker.node_ping != "1":
            continue
        ping = 0
        dustbin_no = dustbin_no + 1
        broker.node_ping = "0"

    elif dustbin_no % 4 == 2:
        if ping == 0:
            broker.publish_on_topics("container3Ping")
            ping = 1
        if broker.node_ping != "1":
            continue
        ping = 0
        dustbin_no = dustbin_no + 1
        broker.node_ping = "0"

    elif dustbin_no % 4 == 3:
        if ping == 0:
            broker.publish_on_topics("container4Ping")
            ping = 1
        if broker.node_ping != "1":
            continue
        ping = 0
        dustbin_no = dustbin_no + 1
        broker.node_ping = "0"
