from random import randint

class Node:
    def __init__(self,value= None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __len__(self):
        curNode = self.head
        index = 0
        while curNode:
            curNode = curNode.next
            index += 1
        return index

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def add(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        # return self.tail

    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))

# customLL = LinkedList()
# customLL.generate(10,0,50)
# print(customLL)
# customLL.add(20)
# print(customLL)
# print(len(customLL))