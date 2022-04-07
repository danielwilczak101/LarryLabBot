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
        t1 = threading.Thread(target=robot.left.turn)
        t1.start()
        t2 = threading.Thread(
            target=robot.right.turn,
            kwargs={"direction": 0}
        )
        t2.start()
    elif key == "right":
        t = threading.Thread(target=robot.right.turn)
        t.start()
        t = threading.Thread(
            target=robot.left.turn,
            kwargs={"direction": 0}
        )
        t.start()
    elif key == "r":
        robot.reverse()


try:
    print("Use up,left,right and down. Down means stop motors")
    listen_keyboard(on_press=press)

# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
