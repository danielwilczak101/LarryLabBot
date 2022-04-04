from time import sleep
from control.robot import robot
import RPi.GPIO as GPIO
import asyncio
from sshkeyboard import listen_keyboard
import random

robot = robot()

distance = 500


async def keyPress(key):
    if key == 'w':
        robot.leftInput = 1
        robot.rightInput = 1
        print("w")
    elif key == 'a':
        robot.rightInput = 1
        robot.leftInput = -1
        print("a")
    elif key == 'd':
        robot.leftInput = 1
        robot.rightInput = -1
        print("d")
    elif key == 's':
        robot.leftInput = -1
        robot.rightInput = -1
        print("s")
    else:
        robot.leftInput = 0
        robot.rightInput = 0
        print("no input")

    await asyncio.sleep(0.001)


async def command():
    robot.leftInput = random.randint(-1, 1)
    robot.rightInput = random.randint(-1, 1)

    robot.left.turn(distance=robot.leftInput * distance)
    robot.right.turn(distance=robot.rightInput * distance)
    await asyncio.sleep(0.001)
    print("command loop")


async def main():
    while True:
        await command()

# Rest of code should be good, just need to figure out how to get listen_keyboard to run async
try:
    print("Use up,left,right and down. Down means stop motors")
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
