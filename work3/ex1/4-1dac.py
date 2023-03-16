import RPi.GPIO as GPIO

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

try:
    while 1:
        num = (input("Input num from 0 to 255 or q for exit\n"))
        if num == 'q':
            break
        elif not num.isdecimal():
            print("you inputed not a decimal num, ERROR")
            continue
        num = int(num)
        if num < 0:
            print("You inputted a negative num, ERROR")
            continue
        print("num is %d" % num)
        print("voltage is %g" % (3.3 / 256 * num))
        GPIO.output(dac, decimal2binary(num))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
