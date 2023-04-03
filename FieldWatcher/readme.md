### Raspberry Pico
1. connect Pico with your computer (MAC/PC/Linux...), which will be recognized as "RPI-RP2"
2. install CircuitPython and copy the necessary modules.
	a) Copy `adafruit-circuitpython-raspberry_pi_pico-en_US-7.0.0.uf2` into your RPI-RP2. Seconds later, the installation will be finished and name will be updated as **Circuitpy**
	b) Copy modules and codes under **codes** folder into the **Circuitpy**.
	c) calibrate the soil moisture sensors by hand
	d) set time with sensor ds3231

<pre>
import board
import adafruit_ds3231
import bitbangio
import time
import digitalio
import busio
import adafruit_tsl2561

i2c = bitbangio.I2C(board.GP13 , board.GP12)
ds3231 = adafruit_ds3231.DS3231(i2c)
current = ds3231.datetime
# set time 16:31 2021/9/27 
ds3231.datetime = time.struct_time((2021, 9, 27, 16, 31, 0, 1, 1, -1))
current = ds3231.datetime
print('The current time is: {}/{}/{} {:02}:{:02}:{:02}'.format(current.tm_mon, current.tm_mday, current.tm_year, current.tm_hour, current.tm_min, current.tm_sec))
</pre>

	d) copy main.py into the **Circuitpy**. After you power it, it will collect sensors data into `FieldWatcher.Pico.sensors.txt` every 30min.

### FAQ

1. Why do you choose CircuitPython, instead of MicroPython?

2.
