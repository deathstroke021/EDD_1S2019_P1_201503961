import os
import subprocess

class Pila:

    def __init__(self, n):
        self.size = n
        self.data = [None] * n
        self.top = -1

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, e):
        if self.top + 1 == self.size:
            raise Exception("Stack overflowed")
        self.top +=1
        self.data[self.top] = e

    def pop(self):
        if self.empty():
            print("Stack underflowed")
        e = self.data[self.top]
        self.top -=1
        return e

    def vaciar(self):
        while self.empty() is False:
            print(self.pop())

    def graphviz(self):
        if self.empty() is True:
            print("Pila vacia")
        else:
            file = open("Stack.dot", "w")
            file.write('digraph firsGraph{\n')
            file.write('node [shape=record];\n')
            file.write('rankdir=LR;\n')
            file.write('node_A [shape=record    label=\"')
            while self.empty() is False:

                file.write('|' + str(self.pop()))
                #print(self.pop())
                #print(self.pop())
            file.write('\"];\n')
            file.write('}')
            file.close()

            os.system('dot Stack.dot -Tpng -o Stack.png')
            #print("Se creo el archivo dot correctamente")
    def show_graphviz(self):
        #subprocess.check_call(['open','Stack.png'])
        #os.popen("Stack.png")
        subprocess.Popen("Stack.png",shell=True)

"""
p = Pila(15)
p.push(15)
p.push(21)
p.push(8)
#p.vaciar()
p.graphviz()"""
