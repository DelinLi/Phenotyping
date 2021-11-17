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


# Set an alarm for 15 seconds from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 900)


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

dht = adafruit_dht.DHT22(board.GP19)
i2c = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c)

ow_bus_dp1 = OneWireBus(board.GP16)
ow_bus_dp2 = OneWireBus(board.GP17)
ow_bus_dp3 = OneWireBus(board.GP18)
devices_dp1 = ow_bus_dp1.scan()
ds18_dp1 = DS18X20(ow_bus_dp1, devices_dp1[0])
devices_dp2 = ow_bus_dp2.scan()
ds18_dp2 = DS18X20(ow_bus_dp2, devices_dp2[0])
devices_dp3 = ow_bus_dp3.scan()
ds18_dp3 = DS18X20(ow_bus_dp3, devices_dp3[0])


i2c = bitbangio.I2C(board.GP13 , board.GP12)
ds3231 = adafruit_ds3231.DS3231(i2c)
current = ds3231.datetime


time.sleep(0.5)
current_time= '{}/{}/{}\t{:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec)

recoder=current_time
recoder=recoder+"\t"+str(ds18_dp1.temperature)+"\t"+str(ds18_dp2.temperature)+"\t"+str(ds18_dp3.temperature)

# setup the moisture sensor power pin and turn it off by default
#sensor_power = DigitalInOut(board.GP7)
#sensor_power.direction = Direction.OUTPUT
#sensor_power.value = False
#sensor_power.value = True

###
# 1. soil moisture
###
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

recoder=recoder+"\t"+str(round(sensor_signal_26.value / 100))+"\t"+str(round(sensor_signal_27.value / 100))+"\t"+str(round(sensor_signal_28.value / 100))

recoder=recoder+"\t"+str(dht.temperature)+"\t"+str(dht.humidity)

recoder=recoder+"\t"+str(light.lux)+"\n"

print(recoder)
f = open('FieldWatcher.Pico.sensors.txt', 'a')
f.write(recoder)
f.close()
led.value = False

alarm.exit_and_deep_sleep_until_alarms(time_alarm)

