from time import sleep
from control.robot import robot
from sshkeyboard import listen_keyboard
import RPi.GPIO as GPIO
import threading
import asyncio

robot = robot()

distance = 500


async def press(key):
    if key == "up":
        robot.leftInput = 1
        robot.rightInput = 1
    elif key == "left":
        robot.rightInput = 1
        robot.leftInput = -1
    elif key == "right":
        robot.leftInput = 1
        robot.rightInput = -1
    elif key == "back":
        robot.leftInput = -1
        robot.rightInput = -1
    else:
        robot.leftInput = 0
        robot.rightInput = 0

    print("key press")


async def command():
    robot.left.turn(robot.leftInput * distance)
    robot.right.turn(robot.rightInput * distance)
    print("command loop")


async def main():
    while True:
        await command()
        await listen_keyboard(on_press=press)

try:
    print("Use up,left,right and down. Down means stop motors")
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
    # listen_keyboard(on_press=press)

# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
