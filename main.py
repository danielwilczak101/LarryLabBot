from time import sleep
from control.robot import robot
import RPi.GPIO as GPIO
import asyncio
from sshkeyboard import listen_keyboard

robot = robot()

distance = 500


async def keyPress():
    if keyboard.is_pressed('w'):
        robot.leftInput = 1
        robot.rightInput = 1
        print("w")
    elif keyboard.is_pressed('a'):
        robot.rightInput = 1
        robot.leftInput = -1
        print("a")
    elif keyboard.is_pressed('d'):
        robot.leftInput = 1
        robot.rightInput = -1
        print("d")
    elif keyboard.is_pressed('s'):
        robot.leftInput = -1
        robot.rightInput = -1
        print("s")
    else:
        robot.leftInput = 0
        robot.rightInput = 0
        print("no input")

    await asyncio.sleep(0.001)

    #print("key press; inputs: " + str(robot.leftInput) + "; " + str(robot.rightInput))


async def command():
    await robot.left.turn(1, robot.leftInput * distance)
    await robot.right.turn(1, robot.rightInput * distance)
    await asyncio.sleep(0.001)
    #print("command loop")


async def main():
    listen_keyboard(on_press=press)
    while True:
        await command()

try:
    print("Use up,left,right and down. Down means stop motors")
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()
