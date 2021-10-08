
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

