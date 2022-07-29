from controls.adafruit_motorkit import MotorKit
from flask import Flask, render_template, jsonify
from picamera2 import Picamera2

import libcamera

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
preview_config["transform"] = libcamera.Transform(vflip=1)
picam2.configure(preview_config)
picam2.still_configuration.size = (320, 240)
picam2.format = 'YUV420'

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
    kit.motor3.throttle = throttle
    kit.motor4.throttle = throttle

    print("forward")
    return 'F'


@app.route('/reverse')
def reverse():
    kit.motor1.throttle = -throttle
    kit.motor2.throttle = -throttle
    kit.motor3.throttle = -throttle
    kit.motor4.throttle = -throttle
    print("reverse")
    return 'R'


@app.route('/left')
def left():
    kit.motor1.throttle = -throttle
    kit.motor2.throttle = throttle
    kit.motor3.throttle = -throttle
    kit.motor4.throttle = throttle
    print("left")
    return 'L'


@app.route('/right')
def right():
    kit.motor1.throttle = throttle
    kit.motor2.throttle = -throttle
    kit.motor3.throttle = throttle
    kit.motor4.throttle = -throttle
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


@app.route('/fwd_diagonal_right')
def fwd_diagonal_right():
    kit.motor1.throttle = throttle
    kit.motor2.throttle = 0
    kit.motor3.throttle = throttle
    kit.motor4.throttle = 0

    print("Forward Diagonal Right")
    return 'FDR'


@app.route('/fwd_diagonal_left')
def fwd_diagonal_left():
    kit.motor1.throttle = 0
    kit.motor2.throttle = throttle
    kit.motor3.throttle = 0
    kit.motor4.throttle = throttle

    print("Forward Diagonal Left")
    return 'FDL'


@app.route('/rev_diagonal_right')
def rev_diagonal_right():
    kit.motor1.throttle = -throttle
    kit.motor2.throttle = 0
    kit.motor3.throttle = -throttle
    kit.motor4.throttle = 0

    print("Reverse Diagonal Right")
    return 'RDR'


@app.route('/rev_diagonal_left')
def rev_diagonal_left():
    kit.motor1.throttle = 0
    kit.motor2.throttle = -throttle
    kit.motor3.throttle = 0
    kit.motor4.throttle = -throttle

    print("Reverse Diagonal Left")
    return 'RDL'


@app.route('/clockwise')
def clockwise():
    kit.motor1.throttle = throttle
    kit.motor2.throttle = -throttle
    kit.motor3.throttle = -throttle
    kit.motor4.throttle = throttle

    print("Spin Left")
    return 'C'


@app.route('/counterclockwise')
def counterclockwise():
    kit.motor1.throttle = -throttle
    kit.motor2.throttle = throttle
    kit.motor3.throttle = throttle
    kit.motor4.throttle = -throttle

    print("Spin Right")
    return 'CC'


@app.route('/camera', methods=['GET'])
def camera():

    picam2.start()
    np_array = picam2.capture_array()
    picam2.stop()

    return jsonify(np_array.tolist())
