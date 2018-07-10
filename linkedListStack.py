'''
Name: Thomas Draves
Date: 07-09-2018
Description: A Linked List that implements a Stack
'''
class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next = None

    #method for setting the data
    def setData(self, data):
        self.data = data
        
    #method for getting data
    def getData(self):
        return self.data

    #method for setting next
    def setNext(self, Next):
        self.next = Next

    #method for getting next
    def getNext(self):
        return self.next

    #method for checking if ther eis a next Node
    def hasNext(self):
        return self.next != None

class Stack(object):
    #constructor
    def __init__(self, data = None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    #method for adding Nodes to top of the Stack
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    #method for taking Nodes off the stack
    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp

    #method for seeing the top off the stack
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()
        return temp
