class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def length(self):
        node = self.head
        index = 0
        while node:
            node = node.next
            index += 1
        return index

    def insert(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None


    def insertionByindex(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.prev = None
                self.head.next.prev = newNode
                newNode.next = self.head
                self.head = newNode

            if location == self.length():
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                newNode.prev = tempNode
                nextNode = tempNode.next
                nextNode.prev = newNode
                tempNode.next = newNode
                newNode.next = nextNode

    def deleteByindex(self,location):
        if self.head == None:
            return "The List is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.next.prev = None

            if location == self.length()-1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    index = 0
                    while index < location-1:
                        node = node.next
                        index += 1
                    self.tail = node
                    node.next = None
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                nextNode = node.next.next
                node.next = nextNode
                nextNode.prev = node





dll = DLinkedList()
dll.insert(1)
dll.insert(2)
#dll.insert(3)

dll.insertionByindex(10000,0)
dll.insertionByindex(10,3)
dll.insertionByindex(3,3)

print([node.value for node in dll])

print(dll.length())


'''Delete By index '''

dll.deleteByindex(1)

print([node.value for node in dll])