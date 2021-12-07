### Raspberry Pico
1. connect Pico with your computer (MAC/PC/Linux...), which will be recognized as "RPI-RP2"
2. install CircuitPython and copy the necessary modules.
  a) Copy `adafruit-circuitpython-raspberry_pi_pico-en_US-7.0.0.uf2` into your RPI-RP2. Seconds later, the installation will be finished and name will be updated as **Circuitpy**
  b) Copy modules and codes under **codes** folder into the **Circuitpy**.
3. explaination of the **codes**



### FAQ
1. Why do you choose CircuitPython, instead of MicroPython?

2.




save power in deep sleep  [done]
https://circuitpython.readthedocs.io/en/latest/shared-bindings/alarm/index.html
https://learn.adafruit.com/deep-sleep-with-circuitpython/alarms-and-sleep

power-management
https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/power-management

import board
import analogio

vbat_voltage = analogio.AnalogIn(board.D9)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2


battery_voltage = get_voltage(vbat_voltage)
print("VBat voltage: {:.2f}".format(battery_voltage))

