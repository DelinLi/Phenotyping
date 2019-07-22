### DHT11 -- Temparature and Humidity
**From oline [**source**](https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/)**
[<img src="/figures/DHT11.jpg"  width="300" height="140">](/Sensors/DHT11/)

#### 1. setup of sensor
DHT11 was used here, it is cheaper but also lower acuracy tha DHT22.
    a. DHT11Range and Acuracy : Humidity:  20---90%, ±5%RH; Temperature 0-50℃,±2℃
    b. Connection: **VCC/+** connect to 3.3V Power (Pin1); **GND/-** connect to Ground(-) (Pin6); **OUT** connect to (Pin7/GPIO4)
#### 2. software Installation
<pre>
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl git

git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python setup.py install

##test command/codes for the DHT11
cd examples
sudo ./AdafruitDHT.py 11 4
Temp=24.0*  Humidity=41.0%

##equally python code
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
</pre>
