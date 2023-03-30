import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimal2binary(x:int, ordinal = 8):
    bin_x = int(bin(x)[2:])
    bin_x = ("%d" % bin_x)[-ordinal:]
    new_len = ordinal - len(bin_x)
    if new_len > 0:
        bin_x = '0' * new_len + bin_x
    bin_x = [int(i) for i in bin_x]
    return bin_x


def adc():
    levels = 2 ** len(dac)
    maxV = 3.3
    summa = 0
    voltage = 0

    for degree in range(7, 0, -1):
        delta_val = 2 ** degree
        summa += delta_val
        signal = decimal2binary(summa)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            summa -= delta_val
    voltage = summa / levels * maxV
    return summa, signal, voltage

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
initial = 0

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        result = adc()
        print("we get {:g} = {}, voltage = {:g}".format(*result))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)

