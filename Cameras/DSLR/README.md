### Control a DSLR with Raspberry Pi [Not Tested yet]
DSLR could offer a much higher picutre quality than [camera of Rapsberry Pi](). And controlling by a Raspberry Pi could make DSLR photoing automatically to make Time_Lapse.

Here, a **libgphoto2** was used to achieve it, however it may not support some cameras.    
[The supported Camera list by **libgphoto2** ](http://www.gphoto.org/proj/libgphoto2/support.php)

#### Online material   
1. [Raspberry Pi Tutorial 41: Control a DSLR with your Pi!  -- Youtube Video](https://www.youtube.com/watch?v=1eAYxnSU2aw)
2. [Raspberry Pi DSLR Camera Control -- Step by Step](https://pimylifeup.com/raspberry-pi-dslr-camera-control/)

#### Installation of **libgphoto2**
<pre>
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install gphoto2
#the python library sh 
pip3 install sh
</pre>

#### Trigger Python Script
Example script [DSLP.RaspPi.py](/Cameras/DSLR/) from [Raspberry Pi Tutorial 41: Control a DSLR with your Pi!  -- Youtube Video](https://www.youtube.com/watch?v=1eAYxnSU2aw)