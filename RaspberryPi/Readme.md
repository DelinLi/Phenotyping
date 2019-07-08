### Command line Installation of OS on Mac  [**From Online source**](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)
*my versionRaspbian GNU/Linux 9.4 (stretch)*
--------
#### Prepare the OS on a SD card

1. Insert SD card (recommend ≥16Gb) into your Mac and dwonload the [**Raspbian**](https://www.raspberrypi.org/downloads/raspbian/)
2. Identify the disk number `diskutil list`
3. Unmout SD card `diskutil unmountDisk /dev/disk<disk# from diskutil> `
4. Copy data to SD card `sudo dd bs=1m if=Your20xx-xx-xx-raspbian-stretch.img of=/dev/rdisk<disk# from diskutil> conv=sync`
5. Eject the SD card `sudo diskutil eject /dev/rdisk<disk# from diskutil>`


#### Set up the Raspberry Tips
1. enable SSH for a headless raspberry pi. vi add an empty file named "**ssh**" to the SD card (**boot**)
2. add an fix IP via add "IP=XXX.XXX.XXX.XXX" to the end of file "**cmdline.txt**" on the SD card (**boot**)
3. For users addressing that could not use the defualt mirrow for **apt-get**. [change mirrors online source](https://blog.csdn.net/la9998372/article/details/77886806/)
<pre>
sudo vi /etc/apt/sources.list
comment the previous files with "#", add:
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi

sudo vi /etc/apt/sources.list.d/raspi.list
comment the previous files with "#", add:
deb http://mirror.tuna.tsinghua.edu.cn/raspberrypi/ stretch main ui
deb-src http://mirror.tuna.tsinghua.edu.cn/raspberrypi/ stretch main ui

sudo apt-get update
</pre>

4. access raspberry pi desktop 
<pre>
1. raspberry pi
sudo apt-get update
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer

sudo raspi-config #enable via "Interfacing Options" -> VNC ->yes

2. Set up VNC on MAC/PC connect with IP
</pre>

5. use VIM (*personaly choice*) `sudo apt-get install vim` and add `alias "vi"="vim"` into ~/.bashrc

-----------
#### How to Clone Raspberry Pi SD Cards Using the Command Line in OS X 
[**From Online source**](https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911)

-----------
#### Build a Python webcam Server [**source**](https://www.instructables.com/id/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/)
<pre>
#installation
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install motion

#configure file "/etc/motion/motion.conf"
daemon on
framerate 1000
stream_port  8081
stream_quality 100
stream_localhost off
webcontrol_localhost off
quality 100
width 640
height 480
post_capture 5
#/etc/default/motion
start_motion_daemon yes

#start
sudo service motion restart
#for unable to find device
sudo modprobe bcm2835-v4l2

#online
XXX.XXX.XXX.yourIP:8081 
</pre>


-----------
#### Sensors
##### Temparature and Humidity
*From oline [**source**](https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/)*

1. setup of sensor 
DHT11 was used here, it is cheaper but also lower acuracy tha DHT22.
    a. DHT11Range and Acuracy : Humidity:  20---90%, ±5%RH; Temperature 0-50℃,±2℃
    b. Connection: **VCC/+** connect to 3.3V Power (Pin1); **GND/-** connect to Ground(-) (Pin6); **OUT** connect to (Pin7/GPIO4)  
2. software Installation 
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

##### Sound sensor [soure](https://www.instructables.com/id/Sound-Sensor-Raspberry-Pi/) 

##### Amazing Xiaomi Mi Flora (花花草草智能检测仪 39RMB 201807JinDong Price)
This is a vey low cost device provide you four factor *tempreature*, *moisture*, *conductivity* and *brightness*. It also provide a free app to read, store those data and give suggestion for your certain plant. Here [MiFlora github project](https://github.com/open-homeautomation/miflora) was used. Also followed steps from [Blog](https://zsiti.eu/xiaomi-miflora-plant-sensor-pimatic-raspberry-pi-3/)

1. get the Mac address of MiLora
<pre>
sudo hcitool lescan
C4:7C:8D:64:76:67 Flower care
</pre>
2. set up the **MiFlora** library (great thanks) 
*assuming you have python3 on your Raspberry Pi*
<pre>
git clone https://github.com/open-homeautomation/miflora.git
cd miflora/
#install depenency
pip3 install btlewrap
#run
python3 demo.py --backend gatttool poll C4:7C:8D:64:76:67
</pre>
#### The RaspberryPi Car
