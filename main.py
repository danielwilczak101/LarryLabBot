from time import sleep
from control.robot import robot
import RPi.GPIO as GPIO
import asyncio
import keyboard

robot = robot()

distance = 500


async def keyPress():
    if keyboard.read_key() == "w":
        robot.leftInput = 1
        robot.rightInput = 1
        print("w")
    elif keyboard.read_key() == "a":
        robot.rightInput = 1
        robot.leftInput = -1
        print("a")
    elif keyboard.read_key() == "d":
        robot.leftInput = 1
        robot.rightInput = -1
        print("d")
    elif keyboard.read_key() == "s":
        robot.leftInput = -1
        robot.rightInput = -1
        print("s")
    else:
        robot.leftInput = 0
        robot.rightInput = 0
        print("no input " + keyboard.read_key())

    #print("key press; inputs: " + str(robot.leftInput) + "; " + str(robot.rightInput))


async def command():
    await robot.left.turn(1, robot.leftInput * distance)
    await robot.right.turn(1, robot.rightInput * distance)
    #print("command loop")


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
