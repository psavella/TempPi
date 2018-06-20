import requests
#import json

urlPost ="http://34.239.113.101:8080/demo/addTemp"
urlLocal ="http://192.168.0.110:8080/demo/addTemp" 

def postData(json_Data):
        r = requests.post(urlLocal,json= json_Data)
        
	print("in Post")
	if r.status_code == requests.codes.ok:
		print("OK")
                print(str(r.status_code))
		return r.status_code
	else:
		print("Not OK")
                print(str(r.status_code))
		return r.status_code

def formatJson(piId,sensorId, dateTime, temperature, humidity):

	json_data = {"device_id":piId,"sensor_id":sensorId,"occurred_ts":str(dateTime),"temp":temperature,"humidity":humidity}
#	Json.dumps(json_data)
	return json_data
