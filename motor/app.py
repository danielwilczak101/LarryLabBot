#from adafruit_motorkit import MotorKit
from flask import Flask, render_template

#kit = MotorKit()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forward')
def forward():
    #kit.motor1.throttle = 0.5
    print("forward")
    return 'Forward'


@app.route('/start')
def start():
    #kit.motor1.throttle = 0.5
    return 'Motor 1 should start'


@app.route('/stop')
def stop():
    #kit.motor1.throttle = 0
    return 'Motor 1 should stop'


@app.route('/reverse')
def reverse():
    #kit.motor1.throttle = -0.5
    return 'Motor 1 should reverse'
