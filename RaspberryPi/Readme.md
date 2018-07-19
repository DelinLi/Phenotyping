### Command line Installation of OS ** ** on Mac  [**From Online source**](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)

--------
#### Prepare the OS on a SD card

1. Insert SD card (recommend ≥16Gb) into your Mac and dwonload the [**Raspbian**](https://www.raspberrypi.org/downloads/raspbian/)
2. Identify the disk number `diskutil list`
3. Unmout SD card `diskutil unmountDisk /dev/disk<disk# from diskutil> `
4. Copy data to SD card `sudo dd bs=1m if=Your20xx-xx-xx-raspbian-stretch.img of=/dev/rdiskdisk# from diskutil> conv=sync`
5. Eject the SD card `sudo diskutil eject /dev/rdisk<disk# from diskutil>`

#### How to Clone Raspberry Pi SD Cards Using the Command Line in OS X 
[**From Online source**](https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911)
