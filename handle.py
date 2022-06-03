import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)  # set pin numbering system

one_low = 5
one_high = 6

two_low = 11
two_high = 9

enable = 26

GPIO.setup(one_low, GPIO.OUT)
GPIO.setup(one_high, GPIO.OUT)
GPIO.setup(two_low, GPIO.OUT)
GPIO.setup(two_high, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)


GPIO.output(enable, GPIO.HIGH)


def linear_out():
    GPIO.output(one_high, GPIO.HIGH)
    GPIO.output(one_low, GPIO.LOW)
    GPIO.output(two_high, GPIO.LOW)
    GPIO.output(two_low, GPIO.HIGH)


def linear_in():
    GPIO.output(one_high, GPIO.LOW)
    GPIO.output(one_low, GPIO.HIGH)
    GPIO.output(two_high, GPIO.HIGH)
    GPIO.output(two_low, GPIO.LOW)


def linear_off():
    GPIO.output(enable, GPIO.LOW)


for _ in range(2):
    print("out")
    linear_out()

    sleep(2)
    print("in")
    linear_in()

GPIO.output(enable, GPIO.LOW)
