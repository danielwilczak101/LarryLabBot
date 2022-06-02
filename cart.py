import RPi.GPIO as GPIO
from time import sleep


pwm = 19
enable = 20
dir = 21

GPIO.setmode(GPIO.BOARD)  # set pin numbering system

GPIO.setup(pwm, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)

GPIO.output(enable, GPIO.HIGH)
GPIO.output(dir, GPIO.HIGH)

pi_pwm = GPIO.PWM(pwm, 1000)  # create PWM instance with frequency
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
