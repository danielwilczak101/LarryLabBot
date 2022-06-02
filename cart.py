
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


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forward')
def forward():
    motor_pwm.ChangeDutyCycle(100)
    print("forward")
    return 'F'


@app.route('/left')
def left():
    GPIO.output(dir, GPIO.HIGH)
    stepper_pwm.ChangeDutyCycle(100)
    print("left")
    return 'L'


@app.route('/right')
def right():
    GPIO.output(dir, GPIO.LOW)
    stepper_pwm.ChangeDutyCycle(100)
    print("right")
    return 'R'


@app.route('/stop')
def stop():
    motor_pwm.ChangeDutyCycle(100)
    print("stop")
    return 'S'
