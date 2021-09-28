import time
import board
from analogio import AnalogIn
 

# setup the moisture sensor power pin and turn it off by default
#sensor_power = DigitalInOut(board.GP7)
#sensor_power.direction = Direction.OUTPUT
#sensor_power.value = False
#sensor_power.value = True

###
# 1. soil moisture 
###
# calibrate the soil moisture sensors by hand
wet_26=300
dry_26=600

wet_27=300
dry_27=600

wet_28=300
dry_28=600

# set the analog read pin for the moisture sensor
sensor_signal_26 = AnalogIn(board.GP26)
print(round(sensor_signal_26.value / 100))
sensor_signal_27 = AnalogIn(board.GP27)
print(round(sensor_signal_27.value / 100))
sensor_signal_28 = AnalogIn(board.GP28)
print(round(sensor_signal_28.value / 100))

while(True):
    print(round(sensor_signal_26.value / 100))
    print(round(sensor_signal_27.value / 100))
    print(round(sensor_signal_28.value / 100))
    print("Wait!")
    time.sleep(6)

