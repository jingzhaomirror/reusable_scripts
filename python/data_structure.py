# Stack implementation as python list, where the top of the stack is the end of the list; supported operations: isEmpty(), push(item), pop(), peek(), size()
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)

# ---------------

# Queue implementation as python list, where the front of the queue (item to be removed) is the end of the list;supported operations: isEmpty(), enqueue(item), dequeue(), size()
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
     
# ----------------

# Deque implementation as python list, where the front of the deque is the end of the list; supported operations: isEmpty(), addFront(item), addRear(item), removeFront(), removeRear(), size()
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
# --------
# unordered list implementation: The basic building block is the node holding at least two pieces of information: 1) its value/data 2) a reference to the next node. A reference to None will denote the fact that there is no next node.
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
     
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
          
class UnorderedList:
    def __init__(self):
        self.head = None
          
    def isEmpty(self):
        return self.head == None
     
    def add(self,item):
    # Since this list is unordered, the specific location of the new item with respect to the other items already in the list is not important
    # it makes sense to place the new item in the easiest location possible which is the head of the list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def append(self, item):
     
    def insert(self, position, item):
    
    def index(self, item):
    
    def pop(self, position=None):
          
# -------------
# ordered list implementation: a collection of items where each item holds a relative position that is based upon some underlying characteristic of the item
# The ordering is typically either ascending or descending and we assume that list items have a meaningful comparison operation that is already defined
# Many of the ordered list operations are the same as those of the unordered list
class OrderedList:
    def __init__(self):
        self.head = None
          
    def isEmpty(self):
        return self.head == None
     
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
          
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
               
    def insert(self, position, item):
    
    def index(self, item):
    
    def pop(self, position=None):
