class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.stack = LinkedList()
        self.minStack = LinkedList()

    def __iter__(self):
        node = self.stack.head
        while node:
            yield node.value
            node = node.next

    def isEmpty(self):
        return self.stack.head is None

    def push(self, value):
        newNode = Node(value)
        if self.stack.head is None:
            self.stack.head = newNode
            self.minStack.head = newNode
        else:
            newNode.next = self.stack.head
            self.stack.head = newNode
            if newNode.value <= self.minStack.head.value:
                newNode.next = self.minStack.head
                self.minStack.head = newNode
            else:
                self.minStack.head.next = newNode

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print([node for node in customStack])
