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


##led blink
def led_sleep(seconds):
    for i in range(seconds):
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ow_bus = OneWireBus(board.GP18)
devices = ow_bus.scan()
ds18 = DS18X20(ow_bus, devices[0])

i2c = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c)

dht = adafruit_dht.DHT22(board.GP19)


#time
i2c = bitbangio.I2C(board.GP13 , board.GP12)
ds3231 = adafruit_ds3231.DS3231(i2c)
current = ds3231.datetime
#print('The current time is: {}/{}/{}\t{:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec))
led_sleep(2)

counts_time=0
while True:
    led.value = True
    counts_time=counts_time+1
    current = ds3231.datetime
    current_time= '{}/{}/{}\t{:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec)
    recoder=str(counts_time)+"\t"+current_time+"\t"+str(ds18.temperature)+"\t"+str(light.lux)+"\t"+str(dht.temperature)+"\t"+str(dht.humidity)+"\n"
    print(recoder)
    f = open('Pico.test05.txt', 'a')
    f.write(recoder)
    f.close()
    led.value = False
    led_sleep(300)




