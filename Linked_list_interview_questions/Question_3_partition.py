'''Write a code to partition a linked list arround a value x
    such that all nodes that are less than x comes before x and rest are after than x '''

from base_structure import *

def partition(ll,target:int):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < target:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode

        curNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None


customLL = LinkedList()
customLL.add(1)
customLL.add(2)
customLL.add(3)
customLL.add(4)
customLL.add(5)
customLL.add(6)
customLL.add(3)
customLL.add(1)
customLL.add(7)
customLL.add(8)
print(customLL)

partition(customLL,3)

print(customLL)


