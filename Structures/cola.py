class Cola:

    def __init__(self, n):
        self.size = n
        self.data = [None] * (n+1)
        self.head = 0
        self.tail = 0

    def _plus_one(self, pointer):
        return (pointer +1) % (self.size +1)

    def _is_empty(self):
        return self.head == self.tail

    def _is_full(self):
        return self._plus_one(self.tail) == self.head

    def enqueue(self, e):
        if self._is_full():
            raise Exception("Queue overflowed")
        self.data[self.tail] = e
        self.tail = self._plus_one(self.tail)

    def dequeue(self):
        if self._is_empty():
            raise Exception("Queue underflowed")
        e = self.data[self.head]
        self.head = self._plus_one(self.head)
        return e

    def print_queue(self):
        print(self.data)

"""
c = Cola(3)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.print_queue()
c.dequeue()
c.dequeue()
c.dequeue()"""
