
from flask import Flask, render_template
from time import sleep
import RPi.GPIO as GPIO
import socket

app = Flask(__name__)

stepper_pwm_pin = 19
enable = 20
dir = 21
motor_pin = 12

GPIO.setmode(GPIO.BCM)  # set pin numbering system
GPIO.setwarnings(False)
GPIO.setup(stepper_pwm_pin, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)
GPIO.setup(motor_pin, GPIO.OUT)

GPIO.output(enable, GPIO.HIGH)
GPIO.output(dir, GPIO.HIGH)

# create PWM instance with frequency
stepper_pwm = GPIO.PWM(stepper_pwm_pin, 15_000)
stepper_pwm.start(0)  # start PWM of required Duty Cycle

motor_pwm = GPIO.PWM(motor_pin, 5_000)  # create PWM instance with frequency
motor_pwm.start(0)  # start PWM of required Duty Cycle


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forward')
def forward():
    motor_pwm.ChangeDutyCycle(50)
    print("forward")
    return 'F'


@app.route('/left')
def left():
    GPIO.output(dir, GPIO.HIGH)
    GPIO.output(enable, GPIO.HIGH)
    for duty in range(0, 100, 1):
        # provide duty cycle in the range 0-100
        stepper_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
    print("left")
    return 'L'


@app.route('/right')
def right():
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(dir, GPIO.LOW)
    for duty in range(0, 100, 1):
        # provide duty cycle in the range 0-100
        stepper_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
    print("right")
    return 'R'


@app.route('/stop')
def stop():
    GPIO.output(enable, GPIO.LOW)
    motor_pwm.ChangeDutyCycle(0)
    print("stop")
    return 'S'
