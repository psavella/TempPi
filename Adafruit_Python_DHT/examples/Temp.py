
#!/usr/bin/python
#pins +=pin2   out=pin11  -=pin6
import sys
import os
import json
import urllib2
import Adafruit_DHT
from datetime import datetime
from filelock import FileLock
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
		data = formatJson(deviceId,SensorId,dateTime,temperature,humidity)
                
                #calls checkWifi, returns true if wifi is enabled
                if checkWifi() == True:
                    
                    #returns result of api call, returns 0 if api not reached, posts data if it is reached
                    result = postData(data)
                    print(json.dumps(data))

                    if result == 200:
                        
                        #opens file with name "usbdrv/storage.txt", or creates it
                        with FileLock(fileName):
                            print("file locked")
                            #reads first line of file
                            f = open(fileName,"a+")
                            line = f.readline().strip()
                            while line:
                                #if there is still a line, line is convertaed to json and posted
                                payload = json.loads(line)
                                postData(payload)
                                line = f.readline().strip()
                            #after loop, os tries to remove file (fails if file does not exist)    
                            f.close()
                        try:
                            os.remove(fileName)
                            print("file deleted")
                        except OSError:
                            pass
                        print("success")
                    #if result is not 200, api must be down, payload is stored locally
                    else:
                        with FileLock(fileName):
                            print("file locked")
                            f = open(fileName,"a+")
                            f.write(json.dumps(data) + "\r\n")
                            f.close()
                        print("temp data stored because failed API connect")
                #if wif is not enabled, payload is stored locally
                else:
                    with FileLock(fileName):
                        print("file locked")
                        f = open(fileName,"a+")
                        f.write(json.dumps(data) + "\r\n")
                        f.close()
                    print("temp data stored because failed wifi connect")
                time.sleep(10)

def checkWifi():
    try:
        #checks if url can be reached
        urllib2.urlopen("http://18.204.21.212:4200", timeout=1)
        return True
    except urllib2.URLError as err:
        return False

getTemp()
