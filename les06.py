import turtle
import tkSimpleDialog
import Tkinter
import random

root = Tkinter.Tk()
root.withdraw()


answer = ''
while answer != 'n':
    answer = tkSimpleDialog.askstring('Draw the circle?', 'y/n')
    if answer == 'y':
        turtle.circle(random.randrange(1, 100))
    else:
        break
