from control.motor import motor


class robot:

    def __init__(self):
        self.left = motor(37, 35)
        self.right = motor(38, 36)

    def forward(self):
        self.left.forward()
        self.right.forward()

    def reverse(self):
        self.left.reverse()
        self.right.reverse()

    def stop(self):
        self.left.stop()
        self.right.stop()
