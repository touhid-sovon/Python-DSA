class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = size * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)

    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0  and self.top == (self.size-1):
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    #enqueue
    def enqueue(self,value):
        if self.isFull():
            return "The Queue is Full"
        elif self.top +1 == self.size:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.queue[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty"

        firstElement = self.queue[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start == self.size-1:
            self.start = 0
        else:
            self.start += 1
        self.queue[start] = None
        return firstElement

    def peek(self):
        if self.isEmpty():
            return "The Queue is empty"
        return self.queue[self.start]

    def delete(self):
        self.queue = self.size * [None]
        self.start = -1
        self.top = -1



customQueue = CircularQueue(5)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)
print(customQueue)

print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue)
customQueue.enqueue(10)
print(customQueue)
print(customQueue.peek())

customQueue.delete()

print(customQueue)