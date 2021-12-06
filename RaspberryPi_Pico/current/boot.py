"""
based on instruction from https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/data-logger
boot.py file for Pico data logging example. If this file is present when
the pico starts up, make the filesystem writeable by CircuitPython. 
-- added a function to detect if usb then do nothing, if no usb then make the filesystem writeable
"""
import storage

storage.remount("/", readonly=False)

import storage
import board
import digitalio

usbpower=digitalio.DigitalInOut(board.GP24)
print(usbpower.value)

if usbpower.value != True:
    print("Hi")
    storage.remount("/", readonly=False)
else:
    print("USB Powering")
