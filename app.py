from adafruit_motorkit import MotorKit
from flask import Flask, render_template
from picamera2 import Picamera2

import socket

kit = MotorKit()
app = Flask(__name__)

throttle = 0.5


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forward')
def forward():
    kit.motor1.throttle = throttle
    kit.motor2.throttle = throttle

    print("forward")
    return 'F'


@app.route('/reverse')
def reverse():
    kit.motor1.throttle = -throttle
    kit.motor2.throttle = -throttle
    print("reverse")
    return 'R'


@app.route('/left')
def left():
    kit.motor1.throttle = -throttle
    kit.motor2.throttle = throttle
    print("left")
    return 'L'


@app.route('/right')
def right():
    kit.motor1.throttle = throttle
    kit.motor2.throttle = -throttle
    print("right")
    return 'R'


@app.route('/stop')
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

    print("stop")
    return 'S'


@app.route('/camera', methods=['GET'])
def camera():
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)

    picam2.start()

    np_array = picam2.capture_array()
    picam2.stop()
    return np_array
