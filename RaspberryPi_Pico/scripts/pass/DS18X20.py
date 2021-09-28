import machine, onewire, ds18x20, time
 
ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
print('Found a ds18x20 device')

temp_10=bytearray(b'(\xe9\x80\x95\xf0\x01<^')
#from print(rom) this is the unique ID of DS18X20
temp_30=bytearray(b'(\xb0\x16\x96\xf0\x01<E')
while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    print(ds_sensor.read_temp(temp_10))
    print(ds_sensor.read_temp(temp_30))
  time.sleep(2)
