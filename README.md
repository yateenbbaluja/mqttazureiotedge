# MQTT-AZURE-IOT-EDGE
This project includes iot edge custom module with controller code with the help of Mqtt

| Languages     | Products               | Page_Type | Description |
| ------------- | -----------------------|-----------|-------------|
| Python        | azure | azure-iot-edge |sample     |This is a sample
                                                     |showing how to deploy a
                                                     |Custom Vision model to a
                                                     |Raspberry Pi 3 device running Azure IoT Edge.|

# TECHNOLOGIES:
  * Azure IoT Edge
  * Docker
  * MQTT
  * Azure Tables
  * Python3
  
# Get started

# To deploy the solution on a Raspberry Pi 3

From your mac or PC:

 1. Clone this sample
 2. Update the .env file with the values for your container registry and make sure that your docker engine has access to it
 3. Build the entire solution by right-clicking on the deployment.template.json file and select Build and push IoT Edge Solution (this can take a     while...especially to build open-cv, numpy and pillow...)
 4. Deploy the solution to your device by right-clicking on the config/deployment.json file, select Create Deployment for Single device and choose your    targeted device
 5. Monitor the messages being sent to the Cloud by right-clicking on your device from the VS Code IoT Edge Extension and select Start Monitoring D2C Message

Note: To stop Device to Cloud (D2C) monitoring, use the Azure IoT Hub: Stop monitoring D2C messages command from the Command Palette (Ctrl+Shift+P).

# To deploy the solution on an x64 PC

From your mac or PC:

 1. Clone this sample
 2. Update the .env file with the values for your container registry and make sure that your docker engine has access to it
 3. Build the entire solution by opening the control palette (Ctrl+Shift+P), select Build and push IoT Edge Solution (this can take a while...especially to build numpy and pillow...) and select the deployment.test-amd64.template.json manifest file (it includes a test video file to simulate a camera)
 4. Deploy the solution to your device by right-clicking on the config/deployment.json file, select Create Deployment for Single device and choose your targeted device
 5. Monitor the messages being sent to the Cloud by right-clicking on your device from the VS Code IoT Edge Extension and select Start Monitoring D2C Message
Note: To stop Device to Cloud (D2C) monitoring, use the Azure IoT Hub: Stop monitoring D2C messages command from the Command Palette (Ctrl+Shift+P).
