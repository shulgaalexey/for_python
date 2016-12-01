import turtle
import tkSimpleDialog
import Tkinter
import random

root = Tkinter.Tk()
root.withdraw()

turtle.speed(0)

def draw_circle(posx, posy, r):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.circle(r)

def fill_circle(posx, posy, radius, r, g, b):
    turtle.fillcolor(r, g, b)
    turtle.begin_fill()
    draw_circle(posx, posy, radius)
    turtle.end_fill()

fill_circle(0, 0, 80, 1, 0, 0)


answer = ''
while answer != 'n':
    answer = tkSimpleDialog.askstring('Draw the circle?', 'y/n')
    if answer == 'y':
        turtle.penup()
        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        for i in range(1, 2):
            turtle.circle(random.randrange(1, 100))
        turtle.end_fill()
    else:
        break
