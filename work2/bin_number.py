import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac     = [26, 19, 13, 6, 5, 11, 9, 10]

number  = [0, 0, 1, 1, 1, 1, 1, 1]


GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)

sleep(7)

GPIO.output(dac, 0)
GPIO.cleanup()