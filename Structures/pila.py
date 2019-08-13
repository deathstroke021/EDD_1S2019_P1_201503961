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

"""
p = Pila(15)
p.push(15)
p.push(21)
p.push(8)
p.vaciar()
"""
