#!/usr/bin/env python3

import subprocess
import time
import os

while True:
	command = "./temperhum.py --nosymbols"
	completed_process = subprocess.run(command, shell=True, text=True, capture_output=True)
	output = completed_process.stdout
	parts = output.split()
	print("temperature: " + parts[0] + "c")
	print("humidity: " + parts[1] + "%")
	print("time: ", time.time())
	time.sleep(60*30)
