##20210924
import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
import busio
import adafruit_tsl2561
import adafruit_dht


print("loaded package")

open("Temp.Pico.csv","r+") as Pico
Pico.write()

# Initialize one-wire bus on board pin D1.
ow_bus = OneWireBus(board.GP18)


# scan for sensors number and ID
devices = ow_bus.scan()
#for device in devices:
#    print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))


#print(devices[0].rom)
#rom_10cm =bytearray(b'(\xe9\x80\x95\xf0\x01<^')
#print(devices[0])

# Scan for sensors and grab the first one found.
ds18 = DS18X20(ow_bus, devices[0])

 
print("Temperature: {0:0.1f}C".format(ds18.temperature))



###light
i2c = busio.I2C(board.GP15, board.GP14)
light = adafruit_tsl2561.TSL2561(i2c)

print('Lux: {}'.format(light.lux))
print('Broadband: {}'.format(light.broadband))
print('Infrared: {}'.format(light.infrared))
print('Luminosity: {}'.format(light.luminosity))

###DHT still work on 
#dht = adafruit_dht.DHT22(board.GP19)
dht = adafruit_dht.DHT22(board.GP28)
print('Air Temperature: {:.1f}C'.format(dht.temperature))
print('Air Humidity: {}%'.format(dht.humidity))

