import csv
import os
import subprocess

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.previous =  None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def add_forward(self,dato):
        if self.empty():
            self.head = self.last = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.next = self.head
            self.head.previous = aux
            self.head = aux

    def add_backward(self, dato):
        if self.empty():
            self.head = self.last = Nodo(dato)
        else:
            aux = self.last
            self.last = aux.next = Nodo(dato)
            self.last.previous = aux
        self.join_nodes()

    def join_nodes(self):
        self.head.previous = self.last
        self.last.next = self.head

    def print_list_forward(self):
        aux = self.head
        while aux:
            print(aux.dato,end='')
            print('->',end='')
            aux = aux.next
            if aux == self.head:
                print(aux.dato)

                break

    def print_list_backward(self):
        aux = self.last
        while aux:
            print(aux.dato,end='')
            print('->',end='')
            aux = aux.previous
            if aux == self.last:
                print(aux.dato)

                break

    def buscar(self, dato):
        aux = self.head
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.next
                if aux == self.head:
                    return false

    def get_head(self):
        aux = self.head
        return aux.dato

    def get_next(self):
        aux = self.head.next
        return aux.dato

    def get_previous(self):
        aux = self.head.previous
        return aux.dato

    def users(self, indice):
        usuarios = []
        aux = self.head
        while aux:
            usuarios.append(aux.dato)
            aux = aux.next
            if aux == self.head:
                break
        return usuarios[indice]

    def users_len(self):
        usuarios = []
        aux = self.head
        while aux:
            usuarios.append(aux.dato)
            aux = aux.next
            if aux == self.head:
                break
        return len(usuarios)

    def graphviz(self):
        if self.head is None:
            print("Lista vacia")
        else:
            file = open("Circulardoublylinkedlist.dot", "w")
            file.write('digraph firsGraph{\n')
            file.write('node [shape=record];\n')
            file.write('rankdir=LR;\n')
            aux = self.head
            count = 0
            while aux:
                #print(aux.dato,end='')
                #print('->',end='')
                file.write('node{} [label=\" {} \"  ];\n'.format(count, aux.dato))
                count+=1
                file.write('node{} -> node{};\n'.format(count-1, count))
                aux = aux.next
                if aux == self.head:
                    #print(aux.dato)
                    #file.write('node{} [label=\" {} \"  ];\n'.format(count, aux.dato))
                    file.write('}')
                    file.close()

                    break

            os.system('dot Circulardoublylinkedlist.dot -Tpng -o Circulardoublylinkedlist.png')
            process = subprocess.Popen(command, stdout=tempFile, shell=True)
            subprocess.check_call(['open','Circulardoublylinkedlist.png'])
            print("Se creo el archivo txt correctamente")


        """if estado == 0:
            aux = self.head
            return aux.dato
        elif estado == 1:
            aux = self.head.next
            return aux.dato
        elif estado == 2:
            aux = self.head.previous
            return aux.dato"""

        """aux = self.head
        while aux:
            print(aux.dato)
            aux = aux.next
            if aux == self.head:
                break"""
"""
print("Usuarios: ")
l = CircularDoublyLinkedList()
l.add_backward("Fernando")
l.add_backward("Maria")
l.add_backward("Veronica")
#l.bulk_loading("Usuarios.csv")
l.print_list_forward()
#l.print_list_backward()
#print(l.print_head())
#print(l.print_next())
#l.graphviz()

print(l.users(0))
print(l.users_len())
l.add_backward("Rocio")
l.print_list_forward()
print(l.users(3))
print(l.users_len())"""
