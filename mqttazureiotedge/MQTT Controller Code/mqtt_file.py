import json
import sys
import time
from queue import Queue
import paho.mqtt.client as mqtt
from SaveData import saveData
from termcolor import colored


class generic_mqtt:
    def __init__(self):
        with open("CONFIG/config.json", "r") as jsonfile:
            self.data = json.load(jsonfile)
            print("Config read successfully")
        self.mqtt_client = mqtt.Client()
        self.q = Queue()
        self.save_data = saveData()
        self.mqtt_connect()

    def on_message(self, client, userdata, msg):
        in_data = json.loads(msg.payload.decode("utf-8"))
        print(colored("Got Data: " + str(in_data), "yellow"))
        self.q.put(in_data)

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.data["TOPIC_SUB"])

    def mqtt_connect(self):
        try:
            self.mqtt_client.username_pw_set(self.data["USER"], self.data["PWD"])
            self.mqtt_client.on_connect = self.on_connect
            self.mqtt_client.on_message = self.on_message
            self.mqtt_client.connect(self.data["URL"], self.data["PORT"])
            self.mqtt_client.loop_start()
            print(colored("Successfully connected to mqtt broker", "green"))
        except KeyError:
            e = sys.exc_info()[0]
            print(colored("Failed to connect to mqtt broker" + str(e), "red"))
            pass

    def mqtt_send_data(self, payload):
        try:
            self.mqtt_client.publish(topic=self.data["TOPIC_PUB"], payload=payload, qos=self.data["QOS"])
            print(colored("Publishing data to mqtt:- " + str(payload), "purple",attrs=['bold']))
            return True
        except:
            e = sys.exc_info()[0]
            print(colored("Exception in sending data to broker:- " + str(e), "red",attrs=['bold']))
            pass

    def send_azure_tables(self):
        if self.q.empty():
            print(colored("Waiting for data from Edge gateway:- ", "blue",attrs=['bold']))
            time.sleep(1)
        if not self.q.empty():
            incoming_data = self.q.get()
            self.save_data.save_into_table(incoming_data)
