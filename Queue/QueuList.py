class Queue:
    def __init__(self):
        self.queue = []

    # display
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)

    # is empty
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    # enqueue
    def enqueue(self,value):
        self.queue.append(value)

    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.queue.pop(0)

    # delete
    def delete(self):
        self.queue = []

    # peek
    def peek(self):
        if self.isEmpty():
            return "The Queue is empty"
        return self.queue[0]


queueList = Queue()
queueList.enqueue(1)
queueList.enqueue(2)
queueList.enqueue(3)
queueList.enqueue(4)
queueList.enqueue(5)

print(queueList)

print(queueList.peek())



