import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.OUT)

GPIO.output(15, 1)

for i in range(10):
    sleep(1)
    if (i % 2 == 0):
        GPIO.output(15, 1)
    else:
        GPIO.output(15, 0)

sleep(10)
GPIO.output(15, 0)

GPIO.cleanup()
        

