class Node:
    #Remember that we do not need to declare our class attributes
    #in Python, only assign those attributes through our constructor
    def __init__(self, id):     #constructor of class Node
        self.id = id            #assign the value sent as a parameter to our class atribute
        self.next = None        #assign the next pointer link to None (null)
        self.previous =  None   #assign the previous pointer link to None (null)

class DoublyLinkedList:
    def __init__(self):         #constructor of class DoublyLinkedList
        self.head = None        #start our list empty, hence our head is None (null)

    #ADD method
    def add(self,node):
        if self.head is None:   #verify if our LinkedList is empty
            self.head = node   #if is empty assign the first node to our head
        else:
            temp = self.head
            while temp.next is not None:    #iterate through our list until
                temp  = temp.next           #-we reach the end of it
            temp.next = node              #assign the next pointer link of the last element to our new element
            node.previous = temp          #assign the previous pointer link of the new element to our last element

    def remove(self):
        if self.head is None:                       #verify if our LinkedList is empty
            print('The list is empty')
        elif self.head.next is None:
            self.head =  None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.previous = None
            temp = None
    #PRINT method
    def print_list(self,direction):
        if self.head is None:                       #verify if our LinkedList is empty
            print('The list is empty')              #print a warning
        else:
            if direction is 'forward':              #check for direction sent as a parameter
                temp = self.head
                while temp.next is not None:        #iterate thru the list to print each element
                    print(temp.id,end='')           #print each element
                    print('->',end='')
                    temp = temp.next
                print(temp.id)
            elif direction is 'backward':           #check for direction sent as a parameter
                temp = self.head
                while temp.next is not None:        #get to the last element of the list
                    temp = temp.next
                while temp.previous is not None:    #iterate backwards thru the list to print each element
                    print(temp.id,end='')           #print each element
                    print('->',end='')
                    temp = temp.previous
                print(temp.id)
            else:
                print('Error, wrong direction to print list specified')
"""
list2 = DoublyLinkedList()      #create a new DoubleLinkedList
list2.add(Node(1))              #add element 1
list2.add(Node(2))              #add element 2
list2.add(Node(3))              #add element 3
list2.print_list('forward')     #print the list forward
#list2.print_list('backward')    #print the list backward
list2.remove()
list2.remove()
list2.print_list('forward')
list2.remove()
list2.print_list('forward')"""
