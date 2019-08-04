class Cola:

    def __init__(self):
        self.datos=[]

    def enqueue(self, dato):
        self.datos.append(dato)

    def dequeue(self):
            try:
                return self.datos.pop(0)
            except:
                raise ValueError("La cola está vacía")

    def print_queue(self):
        print(self.datos)

    def empty(self):
        return self.datos == []

print("Scoreboard: ")
c = Cola()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.print_queue()
c.dequeue()
c.print_queue()
