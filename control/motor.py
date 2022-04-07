import RPi.GPIO as GPIO
from time import sleep
import asyncio

# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)


class motor:

    def __init__(self, DIR, PWM):
        self.DIR = DIR
        self.PWM = PWM
        # Establish Pins in software
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(PWM, GPIO.OUT)
        # Set the first direction you want it to spin
        GPIO.output(DIR, 1)

    def direction(self, direction):
        """Set the direction of the robot."""
        GPIO.output(self.DIR, direction)

    def turn(self, direction=1, distance=500, speed=0.001):
        """Move motor control function"""
        # Esablish the direction you want to go
        GPIO.output(self.DIR, direction)

        # Run for 200 steps. This will change based on how you set you controller
        for _ in range(distance):
            # Set one coil winding to high
            GPIO.output(self.PWM, GPIO.HIGH)
            # Allow it to get there.
            asyncio.sleep(speed)  # Dictates how fast stepper motor will run
            # Set coil winding to low
            GPIO.output(self.PWM, GPIO.LOW)
            asyncio.sleep(speed)  # Dictates how fast stepper motor will run

    def full_speed(self, direction=1):
        """Move the motor full speed."""
        GPIO.output(self.DIR, direction)
        GPIO.output(self.PWM, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.PWM, GPIO.LOW)
