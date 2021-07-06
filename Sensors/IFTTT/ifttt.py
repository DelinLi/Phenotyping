#!/usr/bin/python
## I used this as a python 3 script
## July 6, 2021
## will send to my telegraph messeage and gmail email 
## the two events with same name of "ServerProcess" were set up on IFTTT

import requests
def send_notice(event_name, key, proj,step,server):
	url = "https://maker.ifttt.com/trigger/"+event_name+"/with/key/"+key+""
	payload = "{\n\"value1\":\""+proj+"\",\"value2\":\""+step+"\",\"value3\":\""+server+"\"\n}"
	headers = {'Content-Type': "application/json",
	'User-Agent': "PostmanRuntime/7.15.0",
	'Accept': "*/*",
	'Cache-Control': "no-cache",
	'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
	'Host': "maker.ifttt.com",
	'accept-encoding': "gzip, deflate",
	'content-length': "63",
	'Connection': "keep-alive",
	'cache-control': "no-cache"
	}
	response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
	print(response.text)

text = "This is a test"
key= "Your webhooks key"
send_notice('ServerProcess', key, "Drone","GWAS","SoyCAAS")
