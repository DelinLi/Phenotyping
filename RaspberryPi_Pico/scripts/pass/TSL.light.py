import time
import board
import busio
import adafruit_tsl2561
##based on https://learn.adafruit.com/tsl2561/python-circuitpython
print("loaded package")


###light
i2c = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c)

print('Lux: {}'.format(light.lux))
print('Broadband: {}'.format(light.broadband))
print('Infrared: {}'.format(light.infrared))
print('Luminosity: {}'.format(light.luminosity))

