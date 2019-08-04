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

print("Usuarios: ")
l = CircularDoublyLinkedList()
l.add_backward("Fernando")
l.add_backward("Maria")
l.add_backward("Veronica")
l.print_list_forward()
#print("")
l.print_list_backward()
