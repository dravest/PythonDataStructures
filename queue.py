'''
    Name: Thomas Draves
    Date: 07-17-18
    File Name: queue.py
    Description:
        This class is an implementation of a queue using a
        simple circular array. The head and tail points are
        set to -1 to indicate the queue is empty.
'''

class Queue(object):
    #constructor
    def __init__(self, limit = 5):
        self.que = []
        self.limit = limit
        self.head = None
        self.tail = None
        self.size = 0

    #checks to see if the queue is empty
    def is_empty(self):
        return self.size <= 0

    #adds items to the queue
    def en_queue(self, item):
        if (self.size >= self.limit):
            print('ERROR: Queue Overflow')
            return

        else:
            self.que.append(item)

        if (self.tail is None):
            self.head = self.tail = 0

        else:
            self.tail = self.size

        self.size += 1
        print ('Queue after en_queue', self.que)

    #deletes items from the queue
    def de_queue(self):
        if (self.size <= 0):
            print('ERROR: Queue Underflow')
            return

        else:
            self.que.pop(0)
            self.size -= 1
            if (self.size == 0):
                self.head = self.rear = None

            else:
                self.tail = self.size - 1

            print('Queue after de_queue', self.que)

    #returns the last item added to the queue
    def queue_tail(self):
        if (self.tail is None):
            print('Queue is empty')
            raise IndexError
        
        return self.que[self.tail]

    #returns the next item to leave the queue
    def queue_head(self):
        if (self.head is None):
            print('Queue is empty')
            raise IndexError
        
        return self.que[self.head]

    #returns the size of the queue
    def size(self):
        return self.size
        
