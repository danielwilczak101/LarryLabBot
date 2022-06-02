import RPi.GPIO as GPIO
from time import sleep


stepper_pwm_pin = 19
enable = 20
dir = 21
motor_pin = 12


GPIO.setmode(GPIO.BCM)  # set pin numbering system

GPIO.setup(stepper_pwm_pin, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)
GPIO.setup(motor_pin, GPIO.OUT)

GPIO.output(enable, GPIO.HIGH)
GPIO.output(dir, GPIO.HIGH)

# create PWM instance with frequency
stepper_pwm = GPIO.PWM(stepper_pwm_pin, 5000)
stepper_pwm.start(0)  # start PWM of required Duty Cycle

motor_pwm = GPIO.PWM(motor_pin, 10_000)  # create PWM instance with frequency
motor_pwm.start(0)  # start PWM of required Duty Cycle


print("Running")


def direction(dir):
    """
    This function sets the direction of the stepper motor.
    Right = 1 
    Left = 0
    """
    if dir == 1:
        GPIO.output(dir, GPIO.HIGH)
    elif dir == 0:
        GPIO.output(dir, GPIO.LOW)
    else:
        print("Direction Error")


while True:

    for duty in range(0, 101, 1):
        # provide duty cycle in the range 0-100
        motor_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
