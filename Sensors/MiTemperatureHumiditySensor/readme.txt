## Xiaomi Mi Temperature and Humidity Sensor 
![Xiaomi Mi Temperature and Humidity Sensor](/figures/Mi-Temperature-Humidity-Sensor.jpg)
 

[ratcashdev](https://github.com/ratcashdev) made a libarary named [**mitemp_bt**](https://github.com/ratcashdev/mitemp) for this purpose.


This library gives two choice on Backends from btlewarp: "GatttoolBackend" and "BluepyBackend". The later one is faster in my test (13s vs. 8s).


### set up
sudo pip3 install mqtt-paho
sudo pip3 install psutil
### Codes
see `example.py`

### Example for [read data and upload to ThingSpeak.com]()
see `MiTempHumi_ThingSpeak.py`
