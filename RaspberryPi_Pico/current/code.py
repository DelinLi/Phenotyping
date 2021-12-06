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
sensor_power_one = digitalio.DigitalInOut(board.GP10)
sensor_power_one.direction = digitalio.Direction.OUTPUT
sensor_power_one.value = True
sensor_power_two = digitalio.DigitalInOut(board.GP21)
sensor_power_two.direction = digitalio.Direction.OUTPUT
sensor_power_two.value = True

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

### 2. read the sensors
#### 2.1 air temperature and humidity by DHT22
dht = adafruit_dht.DHT22(board.GP7)

#### 2.2 light by TSL2561
i2c_light = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c_light)

#### 2.3 time by DS3231
try:
    i2c_time = busio.I2C(board.GP13, board.GP12)  # bitbangio.I2C(board.GP13 , board.GP12)
    ds3231 = adafruit_ds3231.DS3231(i2c_time)
    current = ds3231.datetime
    recorder = '{}/{}/{}\t{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour,
                                          current.tm_min)
except:
    recorder = "NA\tNA"


#### 2.4 the soil temperature in two depths
ow_bus_dp = OneWireBus(board.GP18)
devices_dp = ow_bus_dp.scan()

print(devices_dp)
try:
    ds18_dp1 = DS18X20(ow_bus_dp, devices_dp[0])
    temp_dp1 = str(round(ds18_dp1.temperature, 1))
except:
    temp_dp1 = "NA"

try:
    ds18_dp2 = DS18X20(ow_bus_dp, devices_dp[1])
    temp_dp2 = str(round(ds18_dp2.temperature, 1))
except:
    temp_dp2 = "NA"

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
sensor_signal_28 = AnalogIn(board.GP28)  #

#### 2.6 output the sensor reads
time.sleep(1)
light_lux = light.lux  # time.sleep(0.5) is necessary
if light_lux is None:
    light_lux = 0

recorder = recorder + "\t" + temp_dp1 + "\t" + temp_dp2
recorder = recorder + "\t" + str(round(sensor_signal_26.value * conversion_factor, 2)) + "\t" + str(
    round(sensor_signal_28.value * conversion_factor, 2))
recorder = recorder + "\t" + str(round(dht.temperature, 2)) + "\t" + str(round(dht.humidity, 0))
recorder = recorder + "\t" + str(round(light_lux, 0)) + "\n"
print(recorder)
#f = open('FieldWatcher.Pico.sensors.txt', 'a')
#f.write(recorder)
#f.close()

### 3. power off the pin and deep sleep 2h
led.value = False
sensor_power_one.value = False
sensor_power_two.value = False

# Go to deep sleep to save power and set an 2h alarm to reboot.
#time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 7200)
#alarm.exit_and_deep_sleep_until_alarms(time_alarm)



