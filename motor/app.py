from adafruit_motorkit import MotorKit
from flask import Flask

#kit = MotorKit()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Use routes: /start, /stop, /reverse.'


@app.route('/start')
def hello_world():
    #kit.motor1.throttle = 0.5
    return 'Motor 1 should start'


@app.route('/stop')
def hello_world():
    #kit.motor1.throttle = 0
    return 'Motor 1 should stop'


@app.route('/reverse')
def hello_world():
    #kit.motor1.throttle = -0.5
    return 'Motor 1 should reverse'
