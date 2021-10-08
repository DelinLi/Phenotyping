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

# Set an alarm for 15 seconds from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 900)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

ow_bus = OneWireBus(board.GP18)
time.sleep(0.5)
devices = ow_bus.scan()
ds18 = DS18X20(ow_bus, devices[0])

i2c = busio.I2C(board.P15, board.GP14)
time.sleep(0.5)
light = adafruit_tsl2561.TSL2561(i2c)

dht = adafruit_dht.DHT22(board.GP19)
time.sleep(0.5)
#time
i2c = bitbangio.I2C(board.GP13 , board.GP12)
ds3231 = adafruit_ds3231.DS3231(i2c)
current = ds3231.datetime
current_time= '{}/{}/{}\t{:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec)

recoder=current_time+"\t"+str(ds18.temperature)+"\t"+str(light.lux)+"\t"+str(dht.temperature)+"\t"+str(dht.humidity)+"\n"
print(recoder)

f = open('FieldWatcher.Pico.sensors.txt', 'a')
f.write(recoder)
f.close()
led.value = False


# Deep sleep until the alarm goes off. Then restart the program.
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
