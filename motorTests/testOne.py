import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)
pwm.start(0)

pwm.ChangeDutyCycle(5)
sleep(1)
pwm.ChangeDutyCycle(10)
sleep(1)

pwm.stop()
GPIO.cleanup()
