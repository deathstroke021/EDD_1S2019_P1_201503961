class Pila:
    def __init__(self, cantidad):
        self.datos = []
        self.top = -1
        self.cantidad = cantidad

    def push(self, dato):
        if self.top < self.cantidad :
            self.top+=1
            self.datos.append(dato)

    def pop(self):
        if self.top >= 0:
            self.datos.remove(self.datos[self.top])
            self.top-=1

    def print_stack(self):
        print(self.datos)

    def print_top(self):
        print(self.datos[self.top])
        #print(self.datos[self.top],self.top)

print("Scores: ")
p = Pila(3)
p.push(15)
p.push(21)
p.push(8)
p.push(12)
p.print_stack()
p.pop()
p.pop()
p.push(5)
p.print_stack()
p.print_top()
