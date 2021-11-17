import alarm
import time
import board
import digitalio

print("Waking up")


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(10)
led.value = False

# Set an alarm for 60 seconds from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)

# Deep sleep until the alarm goes off. Then restart the program.
alarm.exit_and_deep_sleep_until_alarms(time_alarm)

