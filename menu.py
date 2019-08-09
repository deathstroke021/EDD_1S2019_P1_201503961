from Structures.listadoblecircular import CircularDoublyLinkedList
from Structures.listadoblecircular import Nodo
import curses
import csv

class MenuDisplay:

    def __init__(self, menu):
        # set menu parameter as class property
        self.menu = menu
        # run curses application
        curses.wrapper(self.mainloop)

    def mainloop(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)

        # set screen object as class property
        self.stdscr = stdscr

        # get screen height and width
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(current_row)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:

                    self.print_center("Ingresar Nombre De Usuario:")
                    curses.echo()
                    dato = stdscr.getstr(17,56, 16)
                    usuario = dato.decode("utf-8")
                    #print(usuario)
                    #self.stdscr.getch()
                    #usuario = "Fernando"
                    l.add_backward(usuario)
                    #usuario = l.print_head()
                    #print("Se agrego usuario")

                elif current_row == 1:
                    self.print_center("Mostrando Scoreboard")
                    self.stdscr.getch()

                elif current_row == 2:

                    #self.print_user(l.print_head())

                    if self.confirm_user("Seleccionar Usuario:"):
                        break

                    l.print_list_forward()
                    #l.print_list_backward()

                    print(usuario)
                    #self.stdscr.getch()
                    #print("Se mostro usuarios")

                elif current_row == 3:
                    self.print_center("Mostrando reportes")
                    self.stdscr.getch()
                elif current_row == 4:
                    self.print_center("Se cargo archivo csv, presione ENTER para salir")
                    self.bulk_loading()
                    l.print_list_forward()
                    #l.print_list_backward()

                    self.stdscr.getch()
                elif current_row == len(self.menu) - 1:
                    if self.confirm("Are you sure you want to exit?"):
                        break

            self.print_menu(current_row)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_confirm(self, selected="yes"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "yes"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "no"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "yes"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "yes":
                current_option = "no"
            elif key == curses.KEY_LEFT and current_option == "no":
                current_option = "yes"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "yes" else False

            self.print_confirm(current_option)

    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def print_user(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        x2 = self.screen_width // 3 - len(text) // 2
        y2 = self.screen_height // 2 - 3
        x3 = self.screen_width // 2 - len(text) // 2 + 25
        x4 = self.screen_width // 2 - len(text) // 2 - 6

        self.stdscr.addstr(y2, x4, "Seleccionar usuario:")
        self.stdscr.addstr(y, x2, "<= ")
        self.color_print(y, x, text, 1)
        self.stdscr.addstr(y, x3, " =>")
        #self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

        """
        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_LEFT:
                print("Izquierda")
            elif key == curses.KEY_DOWN:
                print("Derecha")
            elif key == curses.KEY_ENTER:
                print("Usuario seleccionado")
                current_row=3
                self.print_menu(current_row)"""

    def print_confirm_user(self, selected):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 2
        options_width = 10

        usuario = l.print_head()

        # print user
        option = usuario
        x = self.screen_width // 2 - options_width // 2
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print yes
        option = "<="
        x = self.screen_width // 2 - 20
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "=>"
        x = self.screen_width // 2 + 16
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()


    def confirm_user(self, confirmation_text):
        self.print_center(confirmation_text)

        usuario = l.print_head()

        current_option = usuario
        self.print_confirm_user(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == usuario:
                current_option = "=>"
            elif key == curses.KEY_RIGHT and current_option == "<=":
                current_option = usuario
            #elif key == curses.KEY_RIGHT and current_option == "=>":
                #current_option = "=>"
            elif key == curses.KEY_LEFT and current_option == usuario:
                current_option = "<="
            elif key == curses.KEY_LEFT and current_option == "=>":
                current_option = usuario
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return False if current_option == usuario else False

            self.print_confirm_user(current_option)

    def bulk_loading(self):
        with open('Usuarios.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            file = open("Usuarios.txt", "w")

            for row in reader:
                #print(row)

                    l.add_backward(row['Usuario'])

        file.close()



if __name__ == "__main__":

    l = CircularDoublyLinkedList()

    menu = ['1. Play', '2. Scoreboard', '3. User Selection', '4. Reportes', '5. Bulk Loading', '6. Exit']
    MenuDisplay(menu)
