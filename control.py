import RPi.GPIO as GPIO
import json
from pprint import pprint

GPIO.setmode(GPIO.BCM)

with open('config.json') as data_file:    
    data = json.load(data_file)
    for relay in data:
    	GPIO.setup(relay['id'], GPIO.OUT)
    	GPIO.output(relay['id'], relay['on'])
