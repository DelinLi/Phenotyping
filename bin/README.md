### Notification
1. **Python script Gmail.py** send email (an gmail example)
2. **IFTTT -- trigger event**
	* Recive the trigger from ThingSpeak and Send Email Notification. [Create an IFTTT Applet with the **Webhooks** and **email** service.](https://ww2.mathworks.cn/help/thingspeak/analyze-channel-data-to-send-email-notification-from-ifttt.html)   
	* A simple command line also can trigger IFTTT event including Email. `curl   -d '{ "value1":"YourDefinedValue1", "value2":"YourDefinedValue", "value3":"YourDefinedValue3" }' -H "Content-Type: application/json"  -X POST https://maker.ifttt.com/trigger/event/with/key/YourKeyXXX`
