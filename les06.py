import turtle
import tkSimpleDialog
import Tkinter
import random

root = Tkinter.Tk()
root.withdraw()

turtle.speed(0)

answer = ''
while answer != 'n':
    answer = tkSimpleDialog.askstring('Draw the circle?', 'y/n')
    if answer == 'y':
        turtle.penup()
        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200))
        turtle.pendown()
        for i in range(1, 3):
            turtle.circle(random.randrange(1, 100))
    else:
        break
