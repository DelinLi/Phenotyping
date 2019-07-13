from mitemp_bt.mitemp_bt_poller import MiTempBtPoller
from mitemp_bt.mitemp_bt_poller import MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY
from btlewrap import  BluepyBackend

mac="58:2D:34:33:4F:1E" 


poller = MiTempBtPoller(mac, BluepyBackend)

temperature = poller.parameter_value(MI_TEMPERATURE)
humidity = poller.parameter_value(MI_HUMIDITY)
battery = poller.parameter_value(MI_BATTERY)

print(temperature,humidity,battery)
