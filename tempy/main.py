#!/usr/bin/env python3

import subprocess
import time
import datetime
import os

from upload import upload

def ping():
	command = "./temperhum.py --nosymbols"
	completed_process = subprocess.run(command, shell=True, text=True, capture_output=True)
	output = completed_process.stdout
	parts = output.split()
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return parts[0], parts[1], timestamp

while True:
	temperature, humidity, timestamp = ping()
	print("Temperature: ", temperature)
	print("Humidity:    ", humidity)
	print("Timestamp:   ", timestamp)
	upload_result = upload(temperature, humidity, timestamp)
	print(upload_result)
	time.sleep(60*30)
