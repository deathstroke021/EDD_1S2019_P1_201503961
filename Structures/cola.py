import os
import subprocess

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
            print("Queue overflowed")
        self.data[self.tail] = e
        self.tail = self._plus_one(self.tail)

    def dequeue(self):
        if self._is_empty():
            print("Queue underflowed")
        e = self.data[self.head]
        self.head = self._plus_one(self.head)
        return e

    def print_queue(self):
        print(self.data)

    def vaciar(self):
        while self._is_empty() is False:
            print(self.dequeue())

    def graphviz(self):
        if self._is_empty() is True:
            print("cola vacia")
        else:
            file = open("Queue.dot", "w")
            file.write('digraph firsGraph{\n')
            file.write('node [shape=record];\n')
            file.write('rankdir=LR;\n')
            count = 0
            while self._is_empty() is False:
                file.write('node{} [label=\" {} \"];\n'.format(count, str(self.dequeue())))
                count += 1
                file.write('node{} -> node{};\n'.format(count -1, count))
            file.write('node{} [label=\" Null \"];\n'.format(count))
            #file.write('node{} -> node{};\n'.format(count +1, count+2))
            file.write('}')
            file.close()

            os.system('dot Queue.dot -Tpng -o Queue.png')
            #subprocess.check_call(['open','Queue.png'])
            #os.popen("Queue.png")
            subprocess.Popen("Queue.png",shell=True)
            #print("Se creo el archivo dot correctamente")
"""
c = Cola(10)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.graphviz()"""
#c.print_queue()
#c.dequeue()
#c.dequeue()
#c.dequeue()
#print(c._is_full())
#print(c.vaciar())
