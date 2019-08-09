import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import time
import random

stdscr = curses.initscr() #initialize console
stdscr.keypad(1)
dims = stdscr.getmaxyx() #ventana

def game():

    stdscr.nodelay(1)
    head = [1,1]
    body = [head[:]]*3


    stdscr.border()

    direction = 0
    gameover = False
    foodmade = False
    deadcell = body[-1][:]

    while not gameover:

        #print(head) coordenadas cabeza de la serpiente
        #print(body) coordenadas snake

        while not foodmade: # food
            y, x = random.randrange(1, dims[0]-1), random.randrange(1, dims[1]-1) #random en coordenads y,x
            if stdscr.inch(y,x) == ord(' '):
                foodmade = True
                stdscr.addch(y, x, ord('+'))

        if deadcell not in body:
            stdscr.addch(deadcell[0], deadcell[1], ' ')
        stdscr.addch(head[0], head[1], '#')

        action = stdscr.getch() # movimiento snake
        if action == curses.KEY_UP and direction != 1:
            direction = 3
        elif action == curses.KEY_DOWN and direction !=3:
            direction = 1
        elif action == curses.KEY_RIGHT and direction != 2:
            direction = 0
        elif action == curses.KEY_LEFT and direction != 0:
            direction = 2


        if direction == 0:
            head[1] += 1
        elif direction == 2:
            head[1] -= 1
        elif direction == 1:
            head[0] += 1
        elif direction == 3:
            head[0] -= 1

        deadcell = body[-1][:]
        for z in range(len(body)-1, 0,-1):
            body[z] = body[z-1][:]

        body[0] = head[:]

        if stdscr.inch(head[0],head[1]) != ord(' '):
            gameover = True

        stdscr.move(dims[0]-1, dims[1]-1)
        stdscr.refresh() # refrecar pantalla
        time.sleep(0.1)

game()
curses.endwin() #return terminal to previous state
