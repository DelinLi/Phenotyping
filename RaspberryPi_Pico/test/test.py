import alarm
import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
import busio
import adafruit_tsl2561
import adafruit_dht
import digitalio
import adafruit_ds3231
import bitbangio
from analogio import AnalogIn

 
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(1)

 
#### 2.2 light by TSL2561
i2c_light = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c_light)
light_lux=light.lux
if light_lux is None:
    light_lux=0
 
recorder=str(round(light_lux,0))+"\n"
print(recorder)
 
### 3. power up the pin and deep sleep 30 min
led.value = False
 