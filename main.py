import RPi.GPIO as GPIO
from time import sleep

# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)

class motor:
    
    def __init__(self,DIR,PWM):
        self.DIR = DIR
        self.PWM = PWM
        # Establish Pins in software
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(PWM, GPIO.OUT)
        # Set the first direction you want it to spin
        GPIO.output(DIR, 1)
        
    
    def move(self,direction = 0, distance = 100, speed = 0.001):
        # Esablish the direction you want to go
        GPIO.output(self.DIR,direction)

        # Run for 200 steps. This will change based on how you set you controller
        for x in range(distance):
            # Set one coil winding to high
            GPIO.output(self.PWM,GPIO.HIGH)
            # Allow it to get there.
            sleep(speed) # Dictates how fast stepper motor will run
            # Set coil winding to low
            GPIO.output(self.PWM,GPIO.LOW)
            sleep(speed) # Dictates how fast stepper motor will run
            
    def full_speed(self):
        GPIO.output(self.PWM,GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.PWM,GPIO.LOW)

class robot:
    
    def __init__(self):
        self.left = motor(37,35)
        self.right = motor(38,36)
        
    def forward(self):
        self.left.full_speed()
        self.right.full_speed()
    
    def stop(self):
        self.left.stop()
        self.right.stop()
    
    def turn_left(self,distance):
        self.left.stop()
        self.right.stop()
        self.left.move(distance=distance)
    
    

# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0

robot = robot()

try:
    # Run forever.
    while True:
        robot.forward()
        sleep(3)
        robot.turn_left(1000)
        sleep(3)
        
        
# Once finished clean everything up
except KeyboardInterrupt:
    robot.stop()
    print("cleanup")
    GPIO.cleanup()

