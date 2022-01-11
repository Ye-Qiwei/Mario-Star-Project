import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
time.sleep(10800)
'''
GPIO.output(23, GPIO.LOW)
time.sleep(5)
'''
GPIO.cleanup()