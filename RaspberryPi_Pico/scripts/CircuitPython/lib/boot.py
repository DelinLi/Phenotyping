"""
https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/data-logger
boot.py file for Pico data logging example. If this file is present when
the pico starts up, make the filesystem writeable by CircuitPython.
"""

import storage

storage.remount("/", readonly=False)

#rename boot.py under REPL
'''
import os
os.remove("boot.py")
'''
