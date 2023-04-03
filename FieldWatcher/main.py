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
sensor_power_one =  digitalio.DigitalInOut(board.GP10)
sensor_power_one.direction = digitalio.Direction.OUTPUT
sensor_power_one.value = True
sensor_power_two =  digitalio.DigitalInOut(board.GP21)
sensor_power_two.direction = digitalio.Direction.OUTPUT
sensor_power_two.value = True

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(1)

### 2. read the sensors
#### 2.1 air temperature and humidity by DHT22
dht = adafruit_dht.DHT22(board.GP11)

#### 2.2 light by TSL2561
i2c_light = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c_light)
light_lux=light.lux
if light_lux is None:
    light_lux=0

#### 2.3 time by DS3231
i2c_time = busio.I2C(board.GP13, board.GP12)# bitbangio.I2C(board.GP13 , board.GP12)
ds3231 = adafruit_ds3231.DS3231(i2c_time)
current = ds3231.datetime
current_time= '{}/{}/{}\t{:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec)

#### 2.4 the soil temperature in three depths
ow_bus_dp1 = OneWireBus(board.GP16)
ow_bus_dp2 = OneWireBus(board.GP17)
ow_bus_dp3 = OneWireBus(board.GP18)
devices_dp1 = ow_bus_dp1.scan()
ds18_dp1 = DS18X20(ow_bus_dp1, devices_dp1[0])
devices_dp2 = ow_bus_dp2.scan()
ds18_dp2 = DS18X20(ow_bus_dp2, devices_dp2[0])
devices_dp3 = ow_bus_dp3.scan()
ds18_dp3 = DS18X20(ow_bus_dp3, devices_dp3[0])

#### 2.5 the soil moisture in three depths

# calibrate the soil moisture sensors by hand
wet_26=216
dry_26=415

wet_27=212
dry_27=435

wet_28=196
dry_28=430

sensor_signal_26 = AnalogIn(board.GP26)
sensor_signal_27 = AnalogIn(board.GP27)
sensor_signal_28 = AnalogIn(board.GP28)

time.sleep(0.5)

#### 2.6 output the sensor reads
recorder=current_time
recorder=recorder+"\t"+str(round(ds18_dp1.temperature,1))+"\t"+str(round(ds18_dp2.temperature,1))+"\t"+str(round(ds18_dp3.temperature,1))
recorder=recorder+"\t"+str(round(sensor_signal_26.value ,0))+"\t"+str(round(sensor_signal_27.value ,0))+"\t"+str(round(sensor_signal_28.value ,0))
recorder=recorder+"\t"+str(round(dht.temperature,1))+"\t"+str(round(dht.humidity,0))
recorder=recorder+"\t"+str(round(light_lux,0))+"\n"
print(recorder)
f = open('FieldWatcher.Pico.sensors.txt', 'a')
f.write(recorder)
f.close()

### 3. power up the pin and deep sleep 30 min
led.value = False
sensor_power_one.value = False
sensor_power_two.value = False

# Set an alarm for 30 min from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 1800)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
