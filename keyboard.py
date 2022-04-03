#!/usr/bin/env python3
from tkinter import *
import os

# check if
# if os.environ.get('DISPLAY', '') == '':
#    print('no display found. Using :0.0')
#    os.environ.__setitem__('DISPLAY', ':0.0')

main = Tk()


def leftKey(event):
    print("Left key pressed")


def rightKey(event):
    print("Right key pressed")


frame = Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
frame.pack()
main.mainloop()
