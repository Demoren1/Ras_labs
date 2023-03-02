import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
try:
    for loop in range(3):
        for i in leds:           
            GPIO.output(i, 1)
            sleep(0.2)
            GPIO.output(i, 0)
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()