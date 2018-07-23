### Command line Installation of OS on Mac  [**From Online source**](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)

--------
#### Prepare the OS on a SD card

1. Insert SD card (recommend ≥16Gb) into your Mac and dwonload the [**Raspbian**](https://www.raspberrypi.org/downloads/raspbian/)
2. Identify the disk number `diskutil list`
3. Unmout SD card `diskutil unmountDisk /dev/disk<disk# from diskutil> `
4. Copy data to SD card `sudo dd bs=1m if=Your20xx-xx-xx-raspbian-stretch.img of=/dev/rdisk<disk# from diskutil> conv=sync`
5. Eject the SD card `sudo diskutil eject /dev/rdisk<disk# from diskutil>`


#### Set up the Raspberry Tips
1. enable SSH for a headless raspberry pi. vi add an empty file named "**ssh**" to the SD card (**boot**)
2. add an fix IP via add "IIP=XXX.XXX.XXX.XXX" to the end of file "**cmdline.txt**" on the SD card (**boot**)
3. For users addressing that could not use the defualt user. [change mirrors online source](https://blog.csdn.net/la9998372/article/details/77886806/)
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


#### How to Clone Raspberry Pi SD Cards Using the Command Line in OS X 
[**From Online source**](https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911)
