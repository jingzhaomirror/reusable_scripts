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

# Queue implementation as python list, where the front of the queue (item to be removed) is the end of the list;supported operations: isEmpty(), push(item), pop(), peek(), size()
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
     
     
