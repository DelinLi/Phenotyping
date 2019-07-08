from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random

import argparse
import re
import logging
import sys
from datetime import datetime


string.alphanum = 'XXXXXXXXXXXXXXXXXXXX'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "YOUR-CHANNEL-ID"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "YOUR-CHANNEL-WRITEAPIKEY"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "DL-Pi2"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "Your MQTT API Key"

tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey



Mac="Mac Address of your MiFlora"

from btlewrap import available_backends, BluepyBackend, GatttoolBackend, PygattBackend

from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from miflora import miflora_scanner


Time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
poller=MiFloraPoller(Mac,GatttoolBackend)

InfoUpload="filed1="+str("Outside")+"&field2="+str(poller.parameter_value(MI_TEMPERATURE))+"&field3="+str(poller.parameter_value(MI_LIGHT))+"&field4="+str(poller.parameter_value(MI_MOISTURE))+"&field5="+str(poller.parameter_value(MI_CONDUCTIVITY))

try:
	publish.single(topic,InfoUpload,hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
except:
	print("There was an error whild publishing the data")


