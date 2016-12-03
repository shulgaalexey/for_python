#!/usr/bin/env python
import curses
from random import randrange
from collections import namedtuple

# Movement direction
DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3


Point = namedtuple('Point', 'x y')

snek = []


def is_snek_body(x, y):
    for pt in snek:
        if pt.x == x and pt.y == y:
            return True

    return False


def main(win):

    global stdscr

    stdscr = win

    curses.nl()
    curses.noecho()
    stdscr.timeout(0)

    COLS = curses.COLS - 4
    ROWS = curses.LINES - 4

    curses.curs_set(0)

    for i in range(0, 4):
        snek.append(Point(3 + i, 3))

    for i in range(0, len(snek)):
        stdscr.addch(snek[i].y, snek[i].x, ord('*'))

    direction = RIGHT

    food = Point(randrange(0, COLS), randrange(0, ROWS))
    speed = 300

    snek_ch = ord('*')

    while True:

        stdscr.addch(food.y, food.x, ord('#'))

        head = snek[-1]

        headx = int(head.x)
        heady = int(head.y)
        if direction == DOWN:
            heady += 1
        elif direction == UP:
            heady -= 1
        elif direction == LEFT:
            headx -= 1
        elif direction == RIGHT:
            headx += 1

        if headx < 0 or headx >= COLS or heady < 0 or heady >= ROWS:
            break   # GAME OVER

        if is_snek_body(headx, heady):
            break   # GAME OVER

        stdscr.addch(heady, headx, snek_ch)
        snek.append(Point(headx, heady))
        if headx == food.x and heady == food.y:
            while True:
               food = Point(randrange(0, COLS), randrange(0, ROWS))
               if not is_snek_body(food.x, food.y):
                   break

            if len(snek) > 10:
                speed = 200
                snek_ch = ord('@')
            elif len(snek) > 20:
                speed = 100
                snek_ch = ord('8')
            elif len(snek) > 30:
                speed = 50
                snek_ch = ord('0')
        else:
            tail = snek.pop(0)
            stdscr.addch(tail.y, tail.x, ord(' '))

        ch = stdscr.getch()
        if ch == ord('q') or ch == ord('Q'):
            return
        elif ch == ord('s'):
            stdscr.nodelay(0)
        elif ch == ord(' '):
            stdscr.nodelay(1)

        if ch >= 258 and ch <= 261:
            new_direction = ch - 258
            if new_direction == DOWN and direction != UP:
                direction = DOWN
            elif new_direction == UP and direction != DOWN:
                direction = UP
            elif new_direction == LEFT and direction != RIGHT:
                direction = LEFT
            elif new_direction == RIGHT and direction != LEFT:
                direction = RIGHT

        curses.napms(speed)


curses.wrapper(main)

print('\n\n\tGAME OVER\tSCORE: ' + str(len(snek)) + '\n\n')
