import turtle
import tkSimpleDialog
import Tkinter
import random
import math

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

def draw_baraban(): # draw the bullet baraban
    fill_circle(0, 0, 80, .8, .8, .8)
    fill_circle(0, 160, 6, .2, .2, .2)

    phi = 360. / 7
    r = 50.


    # draw the empty bullet holes in baraban
    for i in range(0, 8):
        phi_rad = phi * i * math.pi / 180.0
        fill_circle(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60, 20, .5, .5, .5)


def animate_baraban(start_pos): # animate the rotating baraban
    phi = 360. / 7
    r = 50.

    for i in range(0, random.randrange(7, 100)):
        phi_rad = phi * (i + start_pos) * math.pi / 180.0
        fill_circle(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60, 20, .9, .0, .0)
        fill_circle(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60, 20, .5, .5, .5)

    # draw the latest bullet
    fill_circle(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60, 20, .9, .0, .0)

    # saving bullet pos for further rounds
    start_pos += i
    start_pos %= 7
    return start_pos


draw_baraban()

last_bullet_pos = 0

answer = ''
while answer != 'n':
    answer = tkSimpleDialog.askstring('Lets play a game?', 'y/n')
    if answer == 'y':

        # animate the rotating baraban
        last_bullet_pos = animate_baraban(last_bullet_pos)
        # check if u ded, lik so ded
        if last_bullet_pos % 7 == 0:
            turtle.penup()
            turtle.goto(-50, 200)
            turtle.pendown()
            turtle.write("U DED (x_x)", font=("Arial", 18, "normal"))

    else:
        break
