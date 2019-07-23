### Raspberry Pi Camera Module V2-8 Megapixel   
      
[<img src="https://3c1703fe8d.site.internapcdn.net/newman/csz/news/800/2016/raspberrypir.jpg"  width="300" height="200">](/Sensors/DHT11/)


#### Example code 
##### **bash command)**   
[Official Documentation ofr RaspiCam](https://www.raspberrypi.org/documentation/usage/camera/raspicam/README.md)   

* **[raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md)**   
	Capturing still photographs with the camera module
* **[raspivid](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md)**   
	Capturing video with the camera module
* **[Time-lapse](https://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md)**   
	Taking pictures at regular intervals and stitching them together in to a video
* **[raspiyuv](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspiyuv.md)**   
	Capturing still photographs and generating raw unprocessed image files

<pre>
#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
raspistill -vf -hf -o /home/pi/camera/$DATE.jpg
</pre>	

##### **Python Example**
<pre>
from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()
</pre>