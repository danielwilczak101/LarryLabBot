from time import sleep
from control.robot import robot
import RPi.GPIO as GPIO
import asyncio
import keyboard

robot = robot()

distance = 500


async def keyPress():
    if keyboard.is_pressed('up'):
        robot.leftInput = 1
        robot.rightInput = 1
    elif keyboard.is_pressed('left'):
        robot.rightInput = 1
        robot.leftInput = -1
    elif keyboard.is_pressed('right'):
        robot.leftInput = 1
        robot.rightInput = -1
    elif keyboard.is_pressed('down'):
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
        await keyPress()

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
