class Node:
    def __init__(self,value= None):
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
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
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

    def searchSLL(self,value):
        if self.head == None:
            return "Linked list is empty"
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return index
                node = node.next
                index +=1
            return "Not there"






slinkedlist = SLinkedList()

slinkedlist.insertSLL(1,0)
slinkedlist.insertSLL(2,0)
# slinkedlist.insertSLL(3,0)
# slinkedlist.insertSLL(4,0)
# slinkedlist.insertSLL(6,1)
# slinkedlist.insertSLL(7,1)
# slinkedlist.insertSLL(10,4)

print([node.value for node in slinkedlist])

#slinkedlist.traverseSLL()
#print(slinkedlist.searchSLL(10))

slinkedlist.deletionSLL(1)
print([node.value for node in slinkedlist])