class Node:
    #constructor
    def__init__(self):
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
    
