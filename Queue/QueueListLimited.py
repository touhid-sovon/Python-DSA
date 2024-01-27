class QueueLimit:
    def __init__(self,maxValue):
        self.maxValue = maxValue
        self.queue = []

    # display
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)

    # is empty
    def isEmpty(self):
        if self.queue == []:
            return True
        return False

    # isFull
    def isFull(self):
        if len(self.queue) == self.maxValue:
            return "The queue is Full"

    # enqueue
    def enqueue(self,value):
        if self.isFull():
            return "The queue is full"
        self.queue.append(value)


    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.queue.pop(0)

    # peek
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.queue[0]

customQueue = QueueLimit(4)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
'customQueue.enqueue(4)
print(customQueue.enqueue(5))

print(customQueue)

print(customQueue.dequeue())

