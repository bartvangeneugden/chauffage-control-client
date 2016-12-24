import RPi.GPIO as GPIO
import json
from pprint import pprint

GPIO.setmode(GPIO.BCM)

with open('config.json') as data_file:    
    data = json.load(data_file)
    for relay in data:
    	print "Relay " + str(relay['id'] + 6) + " status: " + str(relay['on'])
    	GPIO.setup(relay['id'] + 6, GPIO.OUT)
    	GPIO.output(relay['id'] + 6, relay['on'])
