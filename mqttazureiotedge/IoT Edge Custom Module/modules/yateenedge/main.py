import datetime, uuid, json, os
from worker.sensor import sensor
from pytz import timezone 
from worker.generic_mqtt import Generic_Mqtt
import time
mqtt = Generic_Mqtt()
sensor_data = sensor()

while True:
    t_data = sensor_data.get_data()
    if t_data[0] == "null":
        print("Resetting the counter")
    else:
        mqtt.MQTT_Send_Data(t_data[0])
        print("Message sent: {}".format(t_data[0]))
        time.sleep(1)