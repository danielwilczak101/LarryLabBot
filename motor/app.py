from adafruit_motorkit import MotorKit
from flask import Flask, render_template

import socket

kit = MotorKit()
app = Flask(__name__)

throttle = 1

# Print the user the current i.p Address
print((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)),
      s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])


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
    return 'Forward'


@app.route('/reverse')
def reverse():
    kit.motor2.throttle = 0
    kit.motor4.throttle = 0

    kit.motor1.throttle = -throttle
    kit.motor3.throttle = throttle
    print("reverse")
    return 'Motor 1 should reverse'


@app.route('/left')
def left():
    kit.motor1.throttle = 0
    kit.motor3.throttle = 0

    kit.motor2.throttle = throttle
    kit.motor4.throttle = -throttle
    print("left")
    return 'Motor 1 should start'


@app.route('/right')
def right():
    kit.motor1.throttle = 0
    kit.motor3.throttle = 0

    kit.motor2.throttle = -throttle
    kit.motor4.throttle = throttle
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
