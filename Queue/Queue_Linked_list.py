class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class QueueLinkedList:
    def __init__(self):
        self.queue = LinkedList()

    def __iter__(self):
        node = self.queue.head
        while node:
            yield node
            node = node.next

    # is empty
    def isEmpty(self):
        if self.queue.head == None:
            return True
        return False

    # enqueue
    def enqueue(self,value):
        newNoode = Node(value)
        if self.queue.head == None:
            self.queue.head = newNoode
            self.queue.tail = newNoode
        else:
            self.queue.tail.next = newNoode
            self.queue.tail = newNoode

    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"

        delNode = self.queue.head.value
        if self.queue.head == self.queue.tail:
            self.queue.head = None
            self.queue.tail = None
        else:
            self.queue.head = self.queue.head.next
        return delNode

    # PEEK
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.queue.head.value



# customQueue = QueueLinkedList()
# print(customQueue.isEmpty())
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
#
# print([node.value for node in customQueue ])
#
# print(customQueue.dequeue())
# print([node.value for node in customQueue ])
#
# print(customQueue.peek())