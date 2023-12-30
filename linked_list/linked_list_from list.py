# class Node:
#     def __init__(self,value = None):
#         self.value = value
#         self.next = None
#
# class SLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next
#
#     def insertData(self,value):
#         newNode = Node(value)
#         if self.head == None:
#             self.head = newNode
#         else:
#             while newNode.next == None:
#                 newNode = newNode.next
#
#             last.next = newNode
#
#     def ListToLL(self,list:list):
#         linked_list = SLinkedList()
#         for i in list:
#             linked_list.insertData(i)
#
#
# sll = SLinkedList()
# sll.ListToLL([1,2,3])
#
#
# class Node:
#     def __init__(self,value = None):
#         self.value = value
#         self.next = None
#
# class SLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next
#
#     def insertData(self,value):
#         newNode = Node(value)
#         if self.head == None:
#             self.head = newNode
#         else:
#             last = self.head
#             while last.next != None:
#                 last = last.next
#             last.next = newNode
#
#     def ListToSLL(self,list:list):
#         linked_list = SLinkedList()
#         for i in list:
#             linked_list.insertData(i)
#         return self.head
#
#
# sll = SLinkedList()
# sll.ListToSLL([1,2,3])
#
# print([node.value for node in sll])
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

    def ListToSLL(self, lst):
        linked_list = SLinkedList()
        for i in lst:
            linked_list.insertData(i)
        return linked_list
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


    def deletingMiddleValue(self):
        n = self.length()
        self.deletionSLL((n // 2) )

sll = SLinkedList()
sll = sll.ListToSLL([1, 2, 3,4])  # Update the sll variable

# Printing the values
print([node.value for node in sll])

print(sll.length())

print(sll.searchSLLByIndex(2))

sll.deletingMiddleValue()

print([node.value for node in sll])


