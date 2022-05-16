from adafruit_motorkit import MotorKit
from flask import Flask, render_template

kit = MotorKit()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forward')
def forward():
    kit.motor2.throttle = 0
    kit.motor4.throttle = 0

    kit.motor1.throttle = 0.5
    kit.motor3.throttle = 0.5

    print("forward")
    return 'Forward'


@app.route('/reverse')
def reverse():
    kit.motor2.throttle = 0
    kit.motor4.throttle = 0

    kit.motor1.throttle = -0.5
    kit.motor3.throttle = -0.5
    print("reverse")
    return 'Motor 1 should reverse'


@app.route('/left')
def left():
    kit.motor1.throttle = 0
    kit.motor3.throttle = 0

    kit.motor2.throttle = 0.5
    kit.motor4.throttle = 0.5
    print("left")
    return 'Motor 1 should start'


@app.route('/right')
def right():
    kit.motor1.throttle = 0
    kit.motor3.throttle = 0

    kit.motor2.throttle = -0.5
    kit.motor4.throttle = -0.5
    print("right")
    return 'Motor 1 should stop'


@app.route('/stop')
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    print("stop")
    return 'Motor 1 should stop'
