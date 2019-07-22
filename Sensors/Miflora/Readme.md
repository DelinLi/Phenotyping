## Realtime Monitor & Recording of **Temperature** & **Light** & **Soil Moisture** & **Conducctivity** Soultion -- The Wieless (Bluetooth) Sensor could last more than one year with one button battery: 
<img src="/figures/MiFlora.jpg"  width="300" height="600">

### Cost effective
**Rapberry Pi 3B (38$) + MiFloral (8$) + ThingSpeak (Free for Non-Commercial) **


##### Amazing Xiaomi Mi Flora (花花草草智能检测仪 39RMB 201807JinDong Price)
This is a vey low cost device, also waterproof, provide you four factor *tempreature*, *moisture*, *conductivity* and *brightness*. It also provide a free app to read, store those data and give suggestion for your certain plant. Here [MiFlora github project](https://github.com/open-homeautomation/miflora) was used. Also followed steps from [Blog](https://zsiti.eu/xiaomi-miflora-plant-sensor-pimatic-raspberry-pi-3/)

1. get the Mac address of MiLora
<pre>
sudo hcitool lescan
C4:7C:8D:64:76:67 Flower care
</pre>
2. set up the **MiFlora** library (great thanks for the contributors) 
*assuming you have python3 on your Raspberry Pi*
<pre>
git clone https://github.com/open-homeautomation/miflora.git
cd miflora/
#install depenency
pip3 install btlewrap
#run
python3 demo.py --backend gatttool poll C4:7C:8D:64:76:67
</pre>


### Version
OS for Raspberry Pi: **Raspbian GNU/Linux 9.4 (stretch)**
Python version 3.5+
