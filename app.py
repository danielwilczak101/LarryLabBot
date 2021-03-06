from adafruit_motorkit import MotorKit
from flask import Flask, render_template

import socket

kit = MotorKit()
app = Flask(__name__)

throttle = 1


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forward')
def forward():
    kit.motor2.throttle = 0
    kit.motor4.throttle = 0

    kit.motor1.throttle = throttle
    kit.motor3.throttle = -throttle

    print("forward")
    return 'F'


@app.route('/reverse')
def reverse():
    kit.motor2.throttle = 0
    kit.motor4.throttle = 0

    kit.motor1.throttle = -throttle
    kit.motor3.throttle = throttle
    print("reverse")
    return 'R'


@app.route('/left')
def left():
    kit.motor1.throttle = 0
    kit.motor3.throttle = 0

    kit.motor2.throttle = throttle
    kit.motor4.throttle = -throttle
    print("left")
    return 'L'


@app.route('/right')
def right():
    kit.motor1.throttle = 0
    kit.motor3.throttle = 0

    kit.motor2.throttle = -throttle
    kit.motor4.throttle = throttle
    print("right")
    return 'R'


@app.route('/stop')
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    print("stop")
    return 'S'


@app.route('/rotate/right')
def rotate_right():
    kit.motor1.throttle = 0
    kit.motor3.throttle = throttle

    kit.motor2.throttle = 0
    kit.motor4.throttle = throttle
    print("rotate right")
    return 'RR'


@app.route('/rotate/left')
def rotate_left():
    kit.motor1.throttle = -throttle
    kit.motor3.throttle = 0

    kit.motor2.throttle = -throttle
    kit.motor4.throttle = 0
    print("rotate left")
    return 'RL'
