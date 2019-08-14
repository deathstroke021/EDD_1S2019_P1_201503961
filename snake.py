import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import time
import random
import csv
from Structures.listadoblecircular import CircularDoublyLinkedList
from Structures.listadoble import DoublyLinkedList
from Structures.listadoble import Node
from Structures.pila import Pila
from Structures.cola import Cola


startlenght = 3
growlenght = 1
score = 0
level = 1

#speed ={"Easy": 0.1, "Medium": 0.06, "Hard": 0.04}
speed ={"Easy": 0.2, "Medium": 0.1, "Hard": 0.05}
difficulty = "Easy"
acceleration = False
l = CircularDoublyLinkedList()
l2 = DoublyLinkedList()
p = Pila(45)
c = Cola(10)
indice = 0
u = []
v = []
u2 = []
s= []
r=[]

stdscr = curses.initscr() #initialize console
stdscr.keypad(1)
dims = stdscr.getmaxyx() #ventana

def game():
    global u
    usuario = u[0]
    stdscr.clear()
    stdscr.nodelay(1)
    head = [1,3]
    body = [head[:]]*startlenght


    stdscr.border()
    stdscr.addstr(0,int(dims[1]/2-11),"User:" +str(usuario)+  " Score:0 Nivel:1")

    direction = 0
    gameover = False
    foodmade = False
    deadcell = body[-1][:]

    while not gameover:

        #print(head) #coordenadas cabeza de la serpiente
        #print(body) #coordenadas snake


        while not foodmade: # food
            y, x = random.randrange(1, dims[0]-1), random.randrange(1, dims[1]-1) #random en coordenads y,x
            type = random.randint(0,100)
            if type <=20:
                type_food = 0
                if stdscr.inch(y,x) == ord(' '):
                    foodmade = True
                    stdscr.addch(y, x, ord('*'))
                    if p.empty() is True:
                        print("pila vacia")
                    else:
                        p.pop()
                    #p.push("(" +str(x)+ "," +str(y)+ ")")
                    if len(v) == 0:
                        v.append(0)
                    else:
                        v.remove(v[0])
                        v.append(0)
            else:
                type_food = 1
                if stdscr.inch(y,x) == ord(' '):
                    foodmade = True
                    stdscr.addch(y, x, ord('+'))
                    p.push("(" +str(x)+ "," +str(y)+ ")")
                    if len(v) == 0:
                        v.append(1)
                    else:
                        v.remove(v[0])
                        v.append(1)


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
            global score
            global level
            global difficulty
            if stdscr.inch(head[0],head[1]) == ord('+'):
                foodmade = False
                score = 1 + score
                if score == 15 and level == 1:
                    difficulty = "Medium"
                    level = level + 1
                    stdscr.addstr(0,int(dims[1]/2-11),"User:"+str(usuario)+ " Score:" +str(score)+" Nivel:"+str(level))
                    stdscr.refresh()
                elif score == 30 and level == 2:
                    difficulty = "Hard"
                    level = level + 1
                    stdscr.addstr(0,int(dims[1]/2-11),"User:"+str(usuario)+" Score:" +str(score)+" Nivel:"+str(level))
                    stdscr.refresh()
                elif score == 45:
                    stdscr.clear() # mensaje gamewin
                    stdscr.nodelay(0)
                    message1 = "You win!!!"
                    message2 = "You got " + str(str(score))+ " points"
                    #message2 = "You got " + str((len(body)-startlenght)/growlenght) + " points"
                    message3= "Press Space to play again"
                    message4= "Press Enter to quit"
                    message5= "Press M to go to the menu"
                    stdscr.addstr(int(dims[0]/2-2), int((dims[1]-len(message1))/2), message1)
                    stdscr.addstr(int(dims[0]/2-1), int((dims[1]-len(message2))/2), message2)
                    stdscr.addstr(int(dims[0]/2), int((dims[1]-len(message3))/2), message3)
                    stdscr.addstr(int(dims[0]/2+1), int((dims[1]-len(message4))/2), message4)
                    stdscr.addstr(int(dims[0]/2+2), int((dims[1]-len(message5))/2), message5)
                    stdscr.refresh()
                    q = 0
                    while q not in [32,10,77,109]:
                        q = stdscr.getch()
                    if q == 32:
                        score = 0
                        level = 1
                        difficulty = "Easy"
                        game()
                    elif q in [77,109]:
                        stdscr.clear()
                        score = 0
                        level = 1
                        difficulty = "Easy"
                        menu()
                else:
                    stdscr.addstr(0,int(dims[1]/2-11),"User:" +str(usuario)+ " Score:" +str(score)+" Nivel:"+str(level))
                    stdscr.refresh()

                for z in range(growlenght):
                    body.append(body[-1]) # aumentar snake

            elif stdscr.inch(head[0],head[1]) == ord('*') and len(body) > 3:
                foodmade = False
                score = score - 1
                stdscr.addstr(0,int(dims[1]/2-11),"User:" +str(usuario)+ " Score:" +str(score)+" Nivel:" +str(level))
                stdscr.refresh()
                for z in range(growlenght):
                    y=[]
                    x=[]
                    coor= str(body[-1])
                    precoory = coor.lstrip("[")
                    count = 0

                    while (precoory[count] is not ","):
                        #print(precoory[count])
                        y.append(precoory[count])
                        count +=1

                    coorinvertida = coor[::-1]
                    #print(coorinvertida)
                    precoorx = coorinvertida.lstrip("]")
                    #print(precoorx)
                    count2 = 0

                    while (precoorx[count2] is not ","):
                        #print(precoorx[count2])
                        x.append(precoorx[count2])
                        count2 +=1

                    #print(coor)

                    #print(int(''.join(y)))

                    #print(int(''.join(x)[::-1]))

                    yc= int(''.join(y))

                    xc= int(''.join(x)[::-1])

                    stdscr.addch(yc, xc, ' ')

                    body.remove(body[-1]) # disminuir snake
            elif stdscr.inch(head[0],head[1]) == ord('*') and len(body) <= 3:
                foodmade = False
            else:
                gameover = True # terminar juego

                for i in range(len(body)):
                    l2.add(Node(body[i]))

                l2.print_list("forward")

                l2.graphviz()

                for i in range(len(body)):
                    l2.remove()

                if v[0] == 0:
                    p.graphviz()
                else:
                    p.pop()
                    p.graphviz()

                if c._is_full() == True:
                    c.dequeue()
                    c.enqueue("(" + str(usuario) + "," + str(score)+ ")")
                    u2.remove(u2[0])
                    s.remove(s[0])
                    r.remove(r[0])
                    u2.append(usuario)
                    s.append(score)
                    r.append("(" + str(usuario) + "," + str(score)+ ")")
                else:
                    c.enqueue("(" + str(usuario) + "," + str(score)+ ")")
                    u2.append(usuario)
                    s.append(score)
                    r.append("(" + str(usuario) + "," + str(score)+ ")")

                score = 0
                level = 1
                difficulty = "Easy"



        stdscr.move(dims[0]-1, dims[1]-1)
        stdscr.refresh() # refrecar pantalla

        if not acceleration: # velocidad del juego
            time.sleep(speed[difficulty])
        else:
            time.sleep(15.*speed[difficulty]/len(body))


    stdscr.clear() # mensaje gameover
    stdscr.nodelay(0)
    message1 = "Game Over"
    message2 = "You got " + str(len(body)-3)+ " points"
    #message2 = "You got " + str((len(body)-startlenght)/growlenght) + " points"
    message3= "Press Space to play again"
    message4= "Press Enter to quit"
    message5= "Press M to go to the menu"
    stdscr.addstr(int(dims[0]/2-2), int((dims[1]-len(message1))/2), message1)
    stdscr.addstr(int(dims[0]/2-1), int((dims[1]-len(message2))/2), message2)
    stdscr.addstr(int(dims[0]/2), int((dims[1]-len(message3))/2), message3)
    stdscr.addstr(int(dims[0]/2+1), int((dims[1]-len(message4))/2), message4)
    stdscr.addstr(int(dims[0]/2+2), int((dims[1]-len(message5))/2), message5)
    stdscr.refresh()
    q = 0
    while q not in [32,10,77,109]:
        q = stdscr.getch()
    if q == 32:
        game()
    elif q in [77,109]:
        stdscr.clear()
        menu()
#game()

def menu(): # menu snake
    stdscr.clear()
    stdscr.nodelay(0)
    selection = -1
    option = 0
    while selection < 0:
        graphics =[0]*6
        graphics[option] = curses.A_REVERSE
        stdscr.addstr(0,int(dims[1]/2-7),"Snake Reloaded")
        stdscr.addstr(int(dims[0]/2-3), int(dims[1]/2-2), "Play", graphics[0])
        stdscr.addstr(int(dims[0]/2-2), int(dims[1]/2-5), "Scoreboard", graphics[1])
        stdscr.addstr(int(dims[0]/2-1), int(dims[1]/2-7), "User Selection", graphics[2])
        stdscr.addstr(int(dims[0]/2), int(dims[1]/2-4), "Reports", graphics[3])
        stdscr.addstr(int(dims[0]/2+1), int(dims[1]/2-6), "Bulk Loading", graphics[4])
        stdscr.addstr(int(dims[0]/2+2), int(dims[1]/2-2), "Exit", graphics[5])
        stdscr.refresh()
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option -1) %6
        elif action == curses.KEY_DOWN:
            option = (option + 1) %6
        elif action == ord("\n"):
            selection = option
    if selection == 0:
        user_verification()
    elif selection == 1:
        scoreboard()
    elif selection == 2:
        user_selection_option()
    elif selection == 3:
        reports()
    elif selection == 4:
        bulk_loading_option()


def instructions():
    stdscr.clear()
    stdscr.nodelay(0)
    lines = ['Use the arrow keys to move', 'Don\'t run into the wall or the snake', '', 'Press Any Key to go Back']
    for z in range(len(lines)):
        stdscr.addstr(int((dims[0]-len(lines))/2 +z), int((dims[1]-len(lines[z]))/2), lines[z])
    stdscr.refresh()
    stdscr.getch()
    menu()

def bulk_loading_option():
    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.addstr(int(dims[0]/2-2), int(dims[1]/2-15),"Ingrese nombre de archivo csv:")
    stdscr.addstr(int(dims[0]/2+10), int(dims[1]/2-15),"Presione ENTER para continuar")
    stdscr.refresh()
    #stdscr.getch()
    curses.echo()
    dato = stdscr.getstr(int(dims[0]/2), int(dims[1]/2-8), 16)
    archivo = dato.decode("utf-8")

    bulk_loading(archivo)
    l.print_list_forward()

    menu()


def bulk_loading(archivo):
    with open(archivo) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            l.add_backward(row['Usuario'])
            #print(row)

def user_selection_option():
    global startlenght, indice, u
    stdscr.clear()
    selection = -1
    option = 0
    while selection < 1:
        stdscr.clear()
        graphics =[0]*2
        graphics[option] = curses.A_REVERSE
        stdscr.addstr(int(dims[0]/2-3), int(dims[1]/2-12),"Usuarios Snake Reloaded ")
        stdscr.addstr(int(dims[0]/2+10), int(dims[1]/2-12),"Presione M para regresar")
        strings = [l.users(indice),  "Seleccionar usuario"]
        for z in range(len(strings)):
            stdscr.addstr(int((dims[0]-len(strings))/2 +z), int((dims[1]-len(strings[z]))/2), strings[z], graphics[z])
        stdscr.refresh()
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option -1) %2
        elif action == curses.KEY_DOWN:
            option = (option + 1) %2
        elif action == ord('\n'):
            user_selection(l.users(indice))
            selection = option
        elif action in [77,109]:
            selection = option
        elif action == curses.KEY_RIGHT:
            if option == 0:
                if indice == int(l.users_len() - 1):
                    indice = 0
                else:
                    indice += 1

        elif action == curses.KEY_LEFT:
            if option == 0:
                if indice == 0:
                    indice = int(l.users_len() - 1)
                else:
                    indice -= 1

        if selection < 1:
            selection = -1
    menu()

def user_selection(usuario):
    global u
    if len(u) == 0:
        u.append(usuario)
    else:
        u.remove(u[0])
        u.append(usuario)
    #print(u[0])

def user_create():
    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.addstr(int(dims[0]/2-2), int(dims[1]/2-13),"Ingrese nombre de usuario:")
    stdscr.addstr(int(dims[0]/2+10), int(dims[1]/2-15),"Presione ENTER para continuar")
    stdscr.refresh()
    #stdscr.getch()
    curses.echo()
    dato = stdscr.getstr(int(dims[0]/2), int(dims[1]/2-8), 16)
    usuario = dato.decode("utf-8")

    l.add_backward(usuario)
    l.print_list_forward()
    u.append(usuario)

    game()

def user_verification():
    global u
    if len(u) == 0:
        user_create()
    else:
        game()

def reports():
    stdscr.clear()
    selection = -1
    option = 0
    while selection < 4:
        stdscr.clear()
        graphics =[0]*5
        graphics[option] = curses.A_REVERSE
        strings = ["Snake report", "Score report", "Scoreboard report", "Users report", "Exit"]
        for z in range(len(strings)):
            stdscr.addstr(int((dims[0]-len(strings))/2 +z), int((dims[1]-len(strings[z]))/2), strings[z], graphics[z])
        stdscr.refresh()
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option -1) %5
        elif action == curses.KEY_DOWN:
            option = (option + 1) %5
        elif action == ord('\n'):
            selection = option
        if selection == 0: # cambiar dificultad del juego
            l2.show_graphviz()
            #print("Reporte snake")
        elif selection == 1:
            p.show_graphviz()
            #print("Reporte punteo")
        elif selection == 2:
            c.graphviz()
            for i in range(len(r)):
                c.enqueue(r[i])
            #print("Reporte scoreboard")

        elif selection == 3:
            l.graphviz()
            #print("Reporte usuarios")
        if selection < 4:
            selection = -1

    menu()

def scoreboard():
    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.addstr(int(dims[0]/2-7), int(dims[1]/2-10),"Name")
    stdscr.addstr(int(dims[0]/2-7), int(dims[1]/2+10),"Score")
    #lines = ['Use the arrow keys to move', 'Don\'t run into the wall or the snake', '', 'Press Any Key to go Back']
    for z in range(len(u2)):
        stdscr.addstr(int((dims[0]-len(u2))/2 +z), int((dims[1])/2-10), u2[z])
    for y in range(len(s)):
        stdscr.addstr(int((dims[0]-len(s))/2 +y), int((dims[1])/2+10), str(s[y]))
    stdscr.refresh()
    stdscr.getch()
    menu()

"""
def user_selection2():
    u = l.get_head()
    #global startlenght, usuarios , indice
    stdscr.clear()
    selection = -1
    option = 0
    while selection < 1:
        stdscr.clear()
        graphics =[0]*2
        graphics[option] = curses.A_REVERSE
        stdscr.addstr(int(dims[0]/2-3), int(dims[1]/2-12),"Usuarios Snake Reloaded ")
        strings = [u,  "Seleccionar usuario"]
        for z in range(len(strings)):
            stdscr.addstr(int((dims[0]-len(strings))/2 +z), int((dims[1]-len(strings[z]))/2), strings[z], graphics[z])
        stdscr.refresh()
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option -1) %2
        elif action == curses.KEY_DOWN:
            option = (option + 1) %2
        elif action == ord('\n'):
            selection = option
        elif action == curses.KEY_RIGHT:
            if option == 0:
                #print("D")
                u = l.get_next()


        elif action == curses.KEY_LEFT:
            if option == 0:
                #print("A")
                u = l.get_previous()

        if selection < 1:
            selection = -1
    menu()"""


def gameoptions():
    global startlenght, growlenght, difficulty, acceleration
    stdscr.clear()
    selection = -1
    option = 0
    while selection < 4:
        stdscr.clear()
        graphics =[0]*5
        graphics[option] = curses.A_REVERSE
        strings = ["Starting snake lenght: " +str(startlenght), "Snake Grown rate: " +str(growlenght), "Difficulty: " +difficulty, "Aceleration:" +str(acceleration), "Exit"]
        for z in range(len(strings)):
            stdscr.addstr(int((dims[0]-len(strings))/2 +z), int((dims[1]-len(strings[z]))/2), strings[z], graphics[z])
        stdscr.refresh()
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option -1) %5
        elif action == curses.KEY_DOWN:
            option = (option + 1) %5
        elif action == ord('\n'):
            selection = option
        elif action == curses.KEY_RIGHT: # cambiar tamaño del snake
            if option == 0 and startlenght < 20:
                startlenght += 1
            elif option == 1 and growlenght < 10:
                growlenght +=1
        elif action == curses.KEY_LEFT: # cambiar tamaño del snake
            if option == 0 and startlenght > 2:
                startlenght -= 1
            elif option == 1 and growlenght > 1:
                growlenght -=1
        if selection == 3: # cambiar dificultad del juego
            acceleration = not acceleration
        elif selection == 2:
            if difficulty == "Easy":
                difficulty = "Medium"
            elif difficulty == "Medium":
                difficulty = "Hard"
            else:
                difficulty = "Easy"
        if selection < 4:
            selection = -1

    menu()

menu()
curses.endwin() #return terminal to previous state
