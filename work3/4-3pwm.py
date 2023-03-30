import RPi.GPIO as GPIO
# from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
# GPIO.output(14, 1)

pwm_inst = GPIO.PWM(14, 1000)
pwm_inst.start(0)

try:
    while 1:
        percent = int(input("Input new dc \n"))
        if percent < 0 or percent > 100:
            continue
        pwm_inst.ChangeDutyCycle(percent)
        print("voltage is %g" % (3.3*percent/100))
finally:
    pwm_inst.stop()
    GPIO.cleanup()