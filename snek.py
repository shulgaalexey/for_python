#!/usr/bin/env python
import curses
from random import randrange


def main(win):

    global stdscr

    stdscr = win

    curses.nl()
    curses.noecho()
    stdscr.timeout(0)

    cols = curses.COLS - 4
    rows = curses.LINES - 4

    snekx = [0] * 4
    sneky = [0] * 4

    for i in range(0, 4):
        snekx[i] = 3 + i
        sneky[i] = 3

    #xpos = [0] * c
    #ypos = [0] * r
    #for j in range(4, -1, -1):
    #    xpos[j] = randrange(0, c) + 2
    #    ypos[j] = randrange(0, r) + 2


    chout = '.'

    while True:
        #x = randrange(0, c) + 2
        #y = randrange(0, r) + 2

        #stdscr.addch(y, x, ord('.'))
        #stdscr.addch(y, x, ord(chout))


        #xpos[j] = x
        #ypos[j] = y

        for i in range(0, len(snekx)):
            stdscr.addch(sneky[i], snekx[i], ord('*'))

        ch = stdscr.getch()
        if ch == ord('q') or ch == ord('Q'):
            return
        elif ch == ord('s'):
            stdscr.nodelay(0)
        elif ch == ord(' '):
            stdscr.nodelay(1)

        if ch == 258: # down
            chout = 'V'
        elif ch == 259: # up
            chout = '^'
        elif ch == 260: # left
            chout = '<'
        elif ch == 261: # right
            chout = '>'

        curses.napms(500)


curses.wrapper(main)
