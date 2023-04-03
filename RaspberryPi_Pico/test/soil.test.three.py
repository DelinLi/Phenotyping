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

### 1. power on the GPIO Pin


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

### 2. read the sensors
#### 2.1 air temperature and humidity by DHT22
dht = adafruit_dht.DHT22(board.GP7)


#### 2.4 the soil temperature in two depths
 
#### 2.5 the soil moisture in two depths
conversion_factor = 3.3 / 65535  # conversion between actual voltage (0-3.3v) and ADC reading value

# calibrate the soil moisture sensors by hand
# wet_26=0.53 #dry voltage
# dry_26=0.82 #wet voltage
# a_26=(100)/(wet_26-dry_26)
# b_26=  a_26*dry_26
# wet_28=196
# dry_28=430

sensor_signal_26 = AnalogIn(board.GP26)  # * a_26 - b_26
sensor_signal_27 = AnalogIn(board.GP27)
sensor_signal_28 = AnalogIn(board.GP28)  #

#### 2.6 output the sensor reads
time.sleep(5)
#### 2.3 time by DS3231
try:
    i2c_time = busio.I2C(board.GP13, board.GP12)  # bitbangio.I2C(board.GP13 , board.GP12)
    ds3231 = adafruit_ds3231.DS3231(i2c_time)
    current = ds3231.datetime
    recorder = '{}/{}/{}\t{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour,
                                          current.tm_min)
except:
    recorder = "NA\tNA"

 

recorder = recorder + "\t" + str(round(sensor_signal_26.value * conversion_factor, 2)) + "\t" + str(
    round(sensor_signal_27.value * conversion_factor, 2))+ "\t" + str(
    round(sensor_signal_28.value * conversion_factor, 2))
recorder = recorder + "\t" + str(round(dht.temperature, 2)) + "\t" + str(round(dht.humidity, 0)) + "\n"
print(recorder)
f = open('FieldWatcher.Pico.sensors.txt', 'a')
f.write(recorder)
f.close()
time.sleep(2)
### 3. power off the pin and deep sleep 2h
led.value = False
 

# Go to deep sleep to save power and set an 30min alarm to reboot.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 1800)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)