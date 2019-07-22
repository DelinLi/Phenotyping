### (ThingSpeak Analyze Channel Data to Send Email Notification from IFTTT](https://ww2.mathworks.cn/help/thingspeak/analyze-channel-data-to-send-email-notification-from-ifttt.html)

Solution for Situation You needs temperature alter of green house? Water reminder for palnt with low soil mositure 
#### ThingSpeak Analyze Channel Data   

Analyze ThingSpeak data with MATLAB. You can use the result of your analysis to trigger web requests. Like the [offical exmaple](https://ww2.mathworks.cn/help/thingspeak/analyze-channel-data-to-send-email-notification-from-ifttt.html) analysis reads two weeks of data to calculate a threshold based on historical data. A measurement lower than 10 percent of the range of data triggers the notification.   
 
 
#### IFTTT -- Recive the trigger and Send Email Notification    

[Create an IFTTT Applet with the **Webhooks** and **email** service.](https://ww2.mathworks.cn/help/thingspeak/analyze-channel-data-to-send-email-notification-from-ifttt.html)   

A simple command line also can trigger IFTTT event.

<pre>
#use curl trigger event and pass value in json format, 
curl   -d '{ "value1":"YourDefinedValue1", "value2":"YourDefinedValue", "value3":"YourDefinedValue3" }' -H "Content-Type: application/json"  -X POST https://maker.ifttt.com/trigger/event/with/key/YourKeyXXXX
</pre>