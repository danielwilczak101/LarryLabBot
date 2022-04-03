from control.motor import motor


class robot:

    def __init__(self):
        self.left = motor(37, 35)
        self.right = motor(38, 36)

    def forward(self):
        self.left.full_speed()
        self.right.full_speed()

    def stop(self):
        self.left.stop()
        self.right.stop()

    def turn_left(self, distance):
        self.left.stop()
        self.right.stop()
        self.left.move(distance=distance)
