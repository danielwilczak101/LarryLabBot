from time import sleep
from control.robot import robot
from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO

robot = robot()


def press(key):
    if key == "up":
        robot.forward()
    elif key == "down":
        robot.stop()
    elif key == "left":
        robot.left.turn(distance=5000)
        robot.right.turn(direction=0, distance=5000)
    elif key == "right":
        robot.right.turn(distance=5000)
        robot.left.turn(direction=0, distance=5000)


try:
    listen_keyboard(on_press=press)

# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
