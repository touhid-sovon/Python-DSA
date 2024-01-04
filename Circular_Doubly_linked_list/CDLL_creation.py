class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    def length(self):
        node = self.head
        index = 0
        while node:
            node = node.next
            index += 1
            if node == self.tail.next:
                return index



    def insert(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = self.tail
            self.tail.next = newNode

    def insertByindex(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == self.length():
                self.head.prev = newNode
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = self.head
            else:
                tempNode = self.head
                index = 0
                while index < location -1 :
                    tempNode = tempNode.next
                    index += 1
                newNode.prev = tempNode
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                nextNode.prev = newNode

    def deleteByindex(self,location):
        if self.head == None:
            return []
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == self.length()-1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head
            else:
                lastNode = self.head
                index = 0
                while index < location-1:
                    lastNode = lastNode.next
                    index += 1
                nextNode = lastNode.next.next
                nextNode.prev = lastNode
                lastNode.next = nextNode













cdll = CDLinkedList()
'''Insert by value'''
cdll.insert(3)
cdll.insert(2)
cdll.insert(1)
cdll.insert(0)

'''Insert By index'''
cdll.insertByindex(4,0)
cdll.insertByindex(5,0)
cdll.insertByindex(6,0)



''' length of linked list '''
# print(cdll.length())

cdll.insertByindex(100,7)
cdll.insertByindex(123,3)
print([node.value for node in cdll])

cdll.deleteByindex(0)
cdll.deleteByindex(7)
cdll.deleteByindex(2)



print('After Deletion')

print([node.value for node in cdll])

print('Prev values of linked list')
print([node.prev.value if node.prev else None for node in cdll])
print('Next values of linked list')
print([node.next.value if node.next else None for node in cdll])

