import RPi.GPIO as GPIO
from time import sleep

ledpin = 19				# PWM pin connected to LED

GPIO.setmode(GPIO.BOARD)  # set pin numbering system
GPIO.setup(ledpin, GPIO.OUT)

GPIO.setup(20, GPIO.HIGH)           # set GPIO24 as an output
GPIO.setup(21, GPIO.HIGH)           # set GPIO24 as an output

pi_pwm = GPIO.PWM(ledpin, 1000)  # create PWM instance with frequency
pi_pwm.start(0)  # start PWM of required Duty Cycle

print("Running")

while True:
    for duty in range(0, 101, 1):
        pi_pwm.ChangeDutyCycle(duty)  # provide duty cycle in the range 0-100
        sleep(0.01)
    sleep(0.5)

    for duty in range(100, -1, -1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)
