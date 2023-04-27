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
        time.sleep(0.01)
        comp_value = GPIO.input(comp)
        # print("comp value is %g" % comp_value)
        if comp_value == 0:
            summa -= delta_val
    voltage = summa / levels * maxV
    return summa, signal, voltage

def get_pre_div_2(voltage):
    our_num = 0
    maxV = 3.3
    ourV = voltage / maxV
    num = ourV * 256
    our_num = 0
    if num > 240:
        return 2 ** 8 - 1

    for i in range(9):
        if 32 * i < num:
            our_num = 2 ** i - 1
        else:
            break
    return our_num
def base_adc(data: list, frequency):
    GPIO.setup(dac, GPIO.OUT)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
    GPIO.setup(comp, GPIO.IN)
    
    tmp_time = time.time()
    abs_time = 0

    try:
        while True:
            result = adc()
            print(result)
            led_num = get_pre_div_2(result[2])
            # print(led_num)
            led_sig = decimal2binary(led_num)
            GPIO.output(leds, led_sig)
            # print("our massive %r" % led_sig)
            if time.time() - tmp_time > frequency:
                tmp_delta = time.time() - tmp_time
                abs_time += tmp_delta
                data.append((result[0], abs_time))
                tmp_time = time.time()
            if result[0] > 245:
                break
        GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
        while True:
            result = adc()
            print(result)
            led_num = get_pre_div_2(result[2])
            # print(led_num)
            led_sig = decimal2binary(led_num)
            GPIO.output(leds, led_sig)
            # print("our massive %r" % led_sig)
            if time.time() - tmp_time > frequency:
                tmp_delta = time.time() - tmp_time
                abs_time += tmp_delta
                data.append((result[0], abs_time))
                tmp_time = time.time()
            if result[0] < 10:
                break

    finally:
        GPIO.output(dac, GPIO.LOW)
        GPIO.output(leds, GPIO.LOW)
        GPIO.cleanup(dac)
        GPIO.cleanup(leds)


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
initial = 0

# base_adc()