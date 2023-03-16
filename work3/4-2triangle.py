import RPi.GPIO as GPIO
from time import sleep

def decimal2binary(x:int, ordinal = 8):
    bin_x = int(bin(x)[2:])
    bin_x = ("%d" % bin_x)[-ordinal:]
    new_len = ordinal - len(bin_x)
    if new_len > 0:
        bin_x = '0' * new_len + bin_x
    bin_x = [int(i) for i in bin_x]
    return bin_x

GPIO.setmode(GPIO.BCM)

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()

GPIO.setup(dac, GPIO.OUT)
period = 2 << len(dac)

try:
    while 1:
        exit_char = input("Input q for exit\n")
        if exit_char == 'q':
            break
        time = float(input("Input time for passing\n"))
        for i in range(period):
            GPIO.output(dac, decimal2binary(i))
            sleep(time / (2 * period))
        for i in range(period , -1, -1):
            GPIO.output(dac, decimal2binary(i))
            sleep(time / (2 * period))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
