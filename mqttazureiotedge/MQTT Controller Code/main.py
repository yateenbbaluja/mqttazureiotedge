from mqtt_file import generic_mqtt

mqtt = generic_mqtt()


def ping_mqtt():
    while 1:
        mqtt.send_azure_tables()


ping_mqtt()
