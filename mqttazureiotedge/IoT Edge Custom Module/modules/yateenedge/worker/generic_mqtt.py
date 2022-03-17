import sys
import json
import paho.mqtt.client as mqtt
from termcolor import colored

class Generic_Mqtt():
    def __init__(self):
        with open("conf.json", "r") as jsonfile:
            self.data = json.load(jsonfile)
            print("Config read successfully")
        self.MQTT_client = mqtt.Client()
        self.MQTT_Connect()

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.data["TOPIC_SUB"])
        print("Subscribe topic mqtt")

    def on_message(self, client, userdata, msg):
        in_data = json.loads(msg.payload.decode("utf-8"))
        print(in_data)


    def MQTT_Connect(self):
        try:
            # temp = self.data["USR"]
            # print(temp)
            self.MQTT_client.username_pw_set(self.data["USER"], self.data["PWD"])
            self.MQTT_client.on_connect = self.on_connect
            self.MQTT_client.on_message = self.on_message
            self.MQTT_client.connect(self.data["URL"], self.data["PORT"])
            self.MQTT_client.loop_start()
            print(colored("Successfully connected to mqtt broker", "green",attrs=['bold']))
        except:
            e = sys.exc_info()[0]
            print(colored("Failed to connect to mqtt broker- " + str(e), "red",attrs=['bold']))
            pass

    def MQTT_Send_Data(self, payload):
        try:
            self.MQTT_client.publish(topic=self.data["TOPIC_PUB"], payload=json.dumps(payload), qos=self.data["QOS"])
            print(colored("Publishing data to mqtt-:" + str(payload), "green"))
            return True
        except:
            e = sys.exc_info()[0]
            print(colored("EXCEPTION IN SENDING DATA BY GENERIC MQTT - " + str(e), "red"))
            pass
