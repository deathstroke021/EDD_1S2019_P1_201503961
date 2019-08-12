class Pila:

    def __init__(self, n):
        self.size = n
        self.data = [None] * n
        self.top = -1


    def push(self, e):
        if self.top + 1 == self.size:
            raise Exception("Stack overflowed")
        self.top +=1
        self.data[self.top] = e

    def pop(self):
        if self.top == -1:
            raise Exception("Stack underflowed")
        e = self.data[self.top]
        self.top -=1
        return e
        
"""
p = Pila(3)
p.push(15)
p.push(21)
p.push(8)
p.pop()
p.pop()
p.pop()"""
