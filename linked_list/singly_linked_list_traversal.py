class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def length(self):
        Node = self.head
        index = 0
        while Node:
            Node = Node.next
            index += 1
        return index

    def insertSLL(self,value,location):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            if location == slinkedlist.length():
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        if self.head == None:
            print("The Linked List is Empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLLByIndex(self,location):
        if self.head == None:
            return "The Linked List is empty"
        elif location > self.length()  :
            return "index is out of range"
        else:
            node = self.head
            index = 0
            while node:
                if index == location:
                    return node.value
                node = node.next
                index +=1

    def deletionSLL(self,location):
        newNode = self.head
        if self.head == None:
            return "Linked list is Empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == (self.length()-1):
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    index = 0
                    while index < (location-1):
                        tempNode = tempNode.next
                        index += 1
                    self.tail = tempNode
                    tempNode.next = None
            else:
                tempNode = self.head
                index = 0
                while index <= (location - 1):
                    prevNode = tempNode
                    tempNode = tempNode.next
                    index += 1
                prevNode.next = tempNode.next

    def deleteAll(self):
        if self.head == None:
            return "The Linked List is Empty"
        else:
            self.head = None
            self.tail = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def deleteNth(self,n:int):
        index = (self.length() - n)
        if self.head == None:
            return []
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif index == self.length()-1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    i = 0
                    while i < (index - 1):
                        tempNode = tempNode.next
                        i += 1
                    self.tail = tempNode
                    tempNode.next = None

            else:
                tempNode = self.head
                i = 0
                while i <= (index - 1):
                    prevNode = tempNode
                    tempNode = tempNode.next
                    i += 1
                prevNode.next = tempNode.next












# sll = SLinkedList()
# node1 = Node(5)
# node2 = Node(6)
#
# sll.head = node1
# sll.head.next = node2
# sll.tail = node2

slinkedlist = SLinkedList()
# slinkedlist.insertSLL(1,1)
slinkedlist.insertSLL(5,0)
slinkedlist.insertSLL(4,0)
slinkedlist.insertSLL(3,0)
slinkedlist.insertSLL(2,0)
slinkedlist.insertSLL(1,0)



# slinkedlist.insertSLL(5,4)
# slinkedlist.insertSLL(100,5)
# slinkedlist.insertSLL(10,1)
# slinkedlist.insertSLL(10,5)



# printing singly linked list
# for node in slinkedlist:
#     print(f"{node.value}",end=" ")

print([node.value for node in slinkedlist])

''' Length of a linked List'''
print(slinkedlist.length())

# slinkedlist.traverseSLL()

#print(slinkedlist.searchSLLByIndex(5))

'''Deletion'''
# slinkedlist.deletionSLL(3)
# print([node.value for node in slinkedlist])
# print(slinkedlist.length())

''' Delete All'''
# slinkedlist.deleteAll()

# print([node.value for node in slinkedlist])

''' reverse '''

#slinkedlist.reverse()

#print([node.value for node in slinkedlist])

'''Delete Nth'''

slinkedlist.deleteNth(1)

print([node.value for node in slinkedlist])