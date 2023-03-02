import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

svet = GPIO.input(14)


if (svet == 0):
    print("Light off")
    GPIO.output(15, 0)
else:
    print("Light on")
    GPIO.output(15, 1)

sleep(10)
GPIO.output(15, 0)

GPIO.cleanup()
