from control.motor import motor

import threading


class robot:

    def __init__(self):
        self.left = motor(38, 36)
        self.right = motor(37, 35)

    def forward(self):
        self.left.forward()
        self.right.forward()

    def reverse(self):
        self.left.reverse()
        self.right.reverse()

    def stop(self):
        self.left.stop()
        self.right.stop()

    def turn_left(self):
        t1 = threading.Thread(target=self.left.turn)
        t1.start()
        t2 = threading.Thread(
            target=self.right.turn,
            kwargs={"direction": 0}
        )
        t2.start()

    def turn_right(self):
        t = threading.Thread(target=self.right.turn)
        t.start()
        t = threading.Thread(
            target=self.left.turn,
            kwargs={"direction": 0}
        )
        t.start()
