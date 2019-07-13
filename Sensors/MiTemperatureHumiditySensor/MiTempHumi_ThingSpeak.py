from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
from datetime import datetime
from btlewrap import  BluepyBackend, GatttoolBackend


from mitemp_bt.mitemp_bt_poller import MiTempBtPoller
from mitemp_bt.mitemp_bt_poller import MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY

string.alphanum = '1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "XXXXXX"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "XXXXXXXX"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "DL-Pi2"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "XXXXXXXX"

tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

# The mac address of your device
Mac="58:2D:34:33:4F:1E" 

# get information from the Device
#poller=MiTempBtPoller(Mac,GatttoolBackend) # works but slower
poller = MiTempBtPoller(Mac, BluepyBackend)

#The "fieldX" vs. Data was defined on your chanel of thingspeak.com
InfoUpload="field1="+str(poller.parameter_value(MI_TEMPERATURE))+"&field2="+str(poller.parameter_value(MI_HUMIDITY))+"&field3="+str(poller.parameter_value(MI_BATTERY))

try:
	publish.single(topic,InfoUpload,hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
	#upload the information onto thingspeak.com 
except:
	print("There was an error whild publishing the data")

