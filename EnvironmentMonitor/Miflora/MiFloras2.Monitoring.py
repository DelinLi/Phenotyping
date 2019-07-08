#!/usr/bin/env python3
"""Demo file showing how to use the miflora library."""

import argparse
import re
import logging
import sys
from datetime import datetime

#define a dictionary to recording MiFloras ID:Mac-address, here I used two for indoor and outdoor 
MiFs={"In":"C4:7C:8D:64:76:67",
"Out":"C4:7C:8D:64:5D:17"}
#local outfile to record the records 
OutFile="/home/pi/Documents/Miflora/Miflora.Recording.txt"

from btlewrap import available_backends, BluepyBackend, GatttoolBackend, PygattBackend

from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from miflora import miflora_scanner

#open outfile and append assuing it has header
#Position	MacAddress	Time	Name	Temperature	Moisture	Light	Conductivity	Battery

f=open(OutFile,"a") 

for Pos in ("In","Out"):
	Mac=MiFs[Pos]
	Time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	poller=MiFloraPoller(Mac,GatttoolBackend)
	f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(Pos,Mac,Time,poller.name(),poller.parameter_value(MI_TEMPERATURE),poller.parameter_value(MI_MOISTURE),poller.parameter_value(MI_LIGHT),poller.parameter_value(MI_CONDUCTIVITY),poller.parameter_value(MI_BATTERY)))

f.close()

