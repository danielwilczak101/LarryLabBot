from time import sleep
from control.robot import robot
from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO
import threading
import asyncio

robot = robot()

left = 0
right = 0
distance = 500


def press(key):
    if key == "up":
        left = 1
        right = 1

    if key == "left":
        right = 1
        left = -1

    if key == "right":
        left = 1
        right = -1

    if key == "back":
        left = -1
        right = -1


def command():
    while True:
        robot.left.turn(left * distance)
        robot.right.turn(right * distance)


try:
    print("Use up,left,right and down. Down means stop motors")
    listen_keyboard(on_press=press)

# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
