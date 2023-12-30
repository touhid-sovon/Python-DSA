class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class CircularSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def length(self):
        node = self.head
        index = 0
        while node:
            node = node.next
            index += 1
            if node == self.head:
                return index

    def insertion(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head

    def insertByindex(self,value,location:int):
        newNode = Node(value)
        if self.head == None:
            return " The list is empty "
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            if location == self.length():
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next =nextNode

    def traverse(self):
        if self.head == None:
            return "This List is Null"
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.head:
                break

    def searchByval(self,value:int):
        if self.head == None:
            return "The linked list is None"
        else:
            node = self.head
            while node:
                if node.value == value:
                    print("YES")
                    return
                node = node.next
                if node == self.head:
                    print("NO")
                    return

    def searchByIndex(self,location):
        if self.head == None:
            return "This Linked list is empty"
        else:
            node = self.head
            index = 0
            while node:
                if index == location:
                    print(node.value)
                    return
                node = node.next
                index += 1
    def deletionByindex(self,location):
        if not self.head :
            return "The linked List Empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head == None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == self.length():
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    index = 0
                    while index < location -1:
                        node = node.next
                        index += 1
                    self.tail = node
                    node.next = self.head
            else:
                node = self.head
                index = 0
                while index <location-1:
                    node = node.next
                    index += 1
                node.next = node.next.next

    def deleteAll(self):
        self.head = None
        self.tail = None











csll = CircularSLinkedList()
csll.insertion(1)
csll.insertion(2)
csll.insertion(3)
csll.insertByindex(0,0)
csll.insertByindex(4,4)
csll.insertByindex(100,5)

print([node.value for node in csll])

print(csll.length())

# '''Traversing Circular Singly Linked List'''
# print('Traverse')
# csll.traverse()

"""search by value"""
#csll.searchByval(12)

'''searchByindex'''

csll.searchByIndex(5)


''' Deletion of Circular Singly Linked List '''

csll.deletionByindex(4)

print([node.value for node in csll])

''' Delete All '''

csll.deleteAll()

print([node.value for node in csll])

