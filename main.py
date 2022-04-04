from time import sleep
from control.robot import robot
from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO
import threading

robot = robot()

left_thread = threading.Thread(target=robot.left.turn)
right_thread = threading.Thread(target=robot.right.turn)


def press(key):
    if key == "up":
        robot.forward()
    elif key == "down":
        robot.stop()
    elif key == "left":
        left_thread.start()
        right_thread.start()
    elif key == "right":
        right_thread.start()


try:
    print("Use up,left,right and down. Down means stop motors")
    listen_keyboard(on_press=press)

# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
