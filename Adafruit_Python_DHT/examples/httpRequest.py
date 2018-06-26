import requests
#import json

urlPost ="http://18.204.21.212:8080/demo/addTemp"
urlLocal ="http://192.168.0.110:8080/demo/addTemp" 

def postData(json_Data):
    try:
        r = requests.post(urlPost,json= json_Data)
        
	print("in Post")
	if r.status_code == requests.codes.ok:
		print("OK")
                print(str(r.status_code))
		return r.status_code
	else:
		print("Not OK")
                print(str(r.status_code))
	        return r.status_code
    except:
        return 0

def formatJson(piId,sensorId, dateTime, temperature, humidity):

	json_data = {"device_id":piId,"sensor_id":sensorId,"occurred_ts":str(dateTime),"temp":temperature,"humidity":humidity}
#	Json.dumps(json_data)
	return json_data
