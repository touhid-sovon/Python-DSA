class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

singlylinkedlist = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlylinkedlist.head = node1
singlylinkedlist.head.next = node2
singlylinkedlist.tail = node2
