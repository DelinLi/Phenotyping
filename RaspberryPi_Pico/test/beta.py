import board
import adafruit_ds3231
import bitbangio
import time
 

i2c = bitbangio.I2C(board.GP13 , board.GP12)
ds3231 = adafruit_ds3231.DS3231(i2c)

ds3231.datetime = time.struct_time((2022, 1, 25, 10, 05, 40, 1, 1, -1))

#current = ds3231.datetime
#print('The current time is: {}/{}/{} {:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec))