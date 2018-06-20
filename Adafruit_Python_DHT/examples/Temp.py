
#!/usr/bin/python
#pins +=pin2   out=pin11  -=pin6
import sys
import Adafruit_DHT
from datetime import datetime
import time
from httpRequest import formatJson
from httpRequest import postData

deviceId = "tempPi1"
SensorId = "Temp1"


def getTemp():
	while True:
                dateTime = datetime.now()
    		humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    		temperature = (temperature * (1.8)) + 32
    		print ("Humidity = {} %; Temperature = {} F".format(humidity, temperature), dateTime)
		json = formatJson(deviceId,SensorId,dateTime,temperature,humidity)
		postData(json)
                time.sleep(600)

getTemp()
