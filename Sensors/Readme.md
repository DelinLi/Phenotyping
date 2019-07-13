## Sensors
I want to collect some sensors that could easily read by raspberry pi (3B+) using python (version 3.5+). This will offer time series data.

### [ThingSpeak.COM](https://github.com/iobridge/thingspeak)
ThingSpeak is an open source “Internet of Things” application and API to store and retrieve data from things using HTTP over the Internet or via a Local Area Network. With ThingSpeak, you can create sensor logging applications, location tracking applications, and a social network of things with status updates. (From [ThingSpeak](https://github.com/iobridge/thingspeak/blob/master/README.textile))

#### [Publish Using WebSockets in Python on a Raspberry Pi  set up for raspberry pi](https://www.mathworks.com/help/thingspeak/use-raspberry-pi-board-that-runs-python-websockets-to-publish-to-a-channel.html)

Please see the [offical documentation](https://www.mathworks.com/help/thingspeak/use-raspberry-pi-board-that-runs-python-websockets-to-publish-to-a-channel.html)) on how to use WebSockets on port 80 to publish to a ThingSpeak™ channel using a Raspberry Pi™ board that runs Python

#### set up
sudo pip3 install mqtt-paho   
sudo pip3 install psutil   

#### Codes Example 
[MiTempHumi_ThingSpeak.py](/Sensors/MiTemperatureHumiditySensor/MiTempHumi_ThingSpeak.py)

### Sensor -- Xiaomi Mi Temperature and Humidity Sensor
![Xiaomi Mi Temperature and Humidity Sensor](/figures/Mi-Temperature-Humidity-Sensor.jpg)
Subject:**Temperature** & **Humidity**    
Bluetooth   
Last more than one year with one AAA battery   


### Sensor -- Xiaomi Mi Flora
![Xiaomi Mi Flora](/figures/MiFlora.jpg)
Subject:**Temperature** & **Light** & **Soil Moisture** & **Conducctivity**   
Bluetooth   
Last more than one year with one button battery   

### Version
OS for Raspberry Pi: **Raspbian GNU/Linux 9.4 (stretch)**   
Python version 3.5+
