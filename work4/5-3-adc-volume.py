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

def get_pre_div_2(voltage):
    our_num = 0
    maxV = 3.2
    ourV = voltage / maxV
    num = ourV * 256
    if num > 240:
        return 2 ** 8 - 1

    for degree in range(9):
        if 2 ** degree < num:
            our_num = 2 ** degree - 1
        else:
            break
    return our_num

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
initial = 0

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        result = adc()
        led_num = get_pre_div_2(result[2])
        led_sig = decimal2binary(led_num)
        GPIO.output(leds, led_sig)
        print("our massive %r" % led_sig)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(dac)
