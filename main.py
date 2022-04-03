from time import sleep
from control.robot import robot

import RPi.GPIO as GPIO

# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0

robot = robot()

try:
    # Run forever.
    while True:
        robot.forward()
        sleep(3)
        robot.turn_left(1000)
        sleep(3)


# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
