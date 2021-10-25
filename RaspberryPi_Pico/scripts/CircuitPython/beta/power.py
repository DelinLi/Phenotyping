import board
import adafruit_ds3231
import bitbangio
import time
import digitalio
import busio
import adafruit_tsl2561

sensor_power =  digitalio.DigitalInOut(board.GP18)
sensor_power.direction = digitalio.Direction.OUTPUT
sensor_power.value = True


#i2c = bitbangio.I2C(board.GP13 , board.GP12)
#ds3231 = adafruit_ds3231.DS3231(i2c)
#current = ds3231.datetime

i2c = busio.I2C(board.GP15, board.GP14)
time.sleep(0.5)
light = adafruit_tsl2561.TSL2561(i2c)
i=0
while i <100:
    time.sleep(5)
    print(light.lux)
    i=i+1
#ds3231.datetime = time.struct_time((2021, 9, 27, 16, 31, 0, 1, 1, -1))
#current = ds3231.datetime
#print('The current time is: {}/{}/{} {:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec))

sensor_power.value = False

