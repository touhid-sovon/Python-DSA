class Node:
    def __init__(self, value=None):
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


    def insertData(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def listToSLL(self, lst):
        linked_list = SLinkedList()
        for i in lst:
            linked_list.insertData(i)
        return linked_list

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

sll = SLinkedList()

sll = sll.listToSLL([1, 2, 3,4])

print([node.value for node in sll])

sll.deleteNth(4)

print([node.value for node in sll])