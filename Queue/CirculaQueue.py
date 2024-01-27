class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = size * [None]
        self.start = -1
        self.top = -1


    def __str__(self):
        # values = []
        # for i in range(self.start,self.top+1):
        #     values.append(str(self.queue[i]))
        values = [str(x) for x in self.queue]
        print(f"Start: {self.start} TOP: {self.top}")
        return ' '.join(values)

    # enqueue
    def enqueue(self,value):
        if self.start == -1:
            self.start += 1
            self.top += 1
            self.queue[self.top] = value
        elif self.start == 0 and self.top < self.size-1:
            self.top += 1
            self.queue[self.top] = value
        elif self.start > 0:
            if self.top == (self.size-1):
                self.top = 0
                self.queue[self.top] = value
            elif (self.top + 1) < self.start:
                self.top += 1
                self.queue[self.top] = value
            else:
                return "The Queue size exceeded"
        else:
            return "The Queue size exceeded"

    # dequeue
    def dequeue(self):
        if self.start == (self.size -1):
            self.start = 0
            return self.queue[self.size -1]
        self.start += 1
        return self.queue[self.start-1]






customCircularqueue = CircularQueue(6)
customCircularqueue.enqueue(1)
customCircularqueue.enqueue(2)
customCircularqueue.enqueue(3)
customCircularqueue.enqueue(4)
customCircularqueue.enqueue(5)
customCircularqueue.enqueue(6)

print(customCircularqueue)

print("The dequeue Value: ",customCircularqueue.dequeue())

print(customCircularqueue)

customCircularqueue.enqueue(7)

print(customCircularqueue)
print(customCircularqueue.dequeue())
print(customCircularqueue.dequeue())
print(customCircularqueue.dequeue())
print(customCircularqueue.dequeue())
print(customCircularqueue.dequeue())
print(customCircularqueue)

