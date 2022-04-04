from time import sleep
from control.robot import robot
import RPi.GPIO as GPIO
import asyncio
import keyboard

robot = robot()

distance = 500


async def keyPress():
    if keyboard.is_pressed('w'):
        robot.leftInput = 1
        robot.rightInput = 1
    elif keyboard.is_pressed('a'):
        robot.rightInput = 1
        robot.leftInput = -1
    elif keyboard.is_pressed('d'):
        robot.leftInput = 1
        robot.rightInput = -1
    elif keyboard.is_pressed('s'):
        robot.leftInput = -1
        robot.rightInput = -1
    else:
        robot.leftInput = 0
        robot.rightInput = 0

    print("key press")


async def command():
    await robot.left.turn(1, robot.leftInput * distance)
    await robot.right.turn(1, robot.rightInput * distance)
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

except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
