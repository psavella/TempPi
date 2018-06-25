
#!/usr/bin/python
#pins +=pin2   out=pin11  -=pin6
import sys
import json
import Adafruit_DHT
from datetime import datetime
import time
from httpRequest import formatJson
from httpRequest import postData

deviceId = "tempPi1"
SensorId = "Temp1"
fileName = "usbdrv/storage.txt"

def getTemp():
	while True:
                dateTime = datetime.now()
    		humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    		temperature = (temperature * (1.8)) + 32
    		print ("Humidity = {} %; Temperature = {} F".format(humidity, temperature), dateTime)
		data = formatJson(deviceId,SensorId,dateTime,temperature,humidity)
                result = postData(data)
                if result == 200:
                    with open(fileName) as f:
                        line = f.readline().strip()
                        while line:
                            print(line)
                            payload = json.loads(line)
                            postData(payload)
                            line = f.readline().strip()
                        try:
                            os.remove(fileName)
                        except OSError:
                            pass
                    print("success")
                else:
                    f = open(fileName,"a+")
                    f.write(json.dumps(data) + "\r\n")
                    f.close()
                    print("failed")
                
                time.sleep(60)

getTemp()
