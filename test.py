from time import sleep
from control.robot import robot
from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO
import threading

robot = robot()


def press(key):
    if key == "up":
        robot.forward()
    elif key == "down":
        robot.stop()
    elif key == "left":
        robot.left.turn(distance=500)
    elif key == "right":
        robot.right.turn(distance=500)


try:
    print("Use up,left,right and down. Down means stop motors")
    listen_keyboard(on_press=press)

# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
