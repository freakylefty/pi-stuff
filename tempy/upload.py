import datetime
import requests
import json

def upload(temperature, humidity, timestamp):
	url = "https://example.com/upload"
	payload = json.dumps( {"temperature": temperature, "humidity": humidity, "timestamp": timestamp} )
	headers = {
	    'content-type': "application/json",
	    'cache-control': "no-cache"
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	return response.text
