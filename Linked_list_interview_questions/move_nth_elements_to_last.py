from base_structure import *

def nthTolast(ll,n):
    if ll.head is None:
        return
    else:
        if n == 0:
            ll.tail.next = ll.head
            ll.tail = ll.tail.next
            ll.head = ll.head.next
            print(ll.head.value,ll.tail.value)
            return ll
        elif n == len(ll)-1:
            return ll
        else:
            tempNode = ll.head
            index = 0
            while index < n-1:
                tempNode = tempNode.next
                index += 1
            moveNode = tempNode.next
            tempNode.next = tempNode.next.next
            ll.tail.next = moveNode
            ll.next = moveNode
            return ll



cutomLL = LinkedList()
cutomLL.add(1)
cutomLL.add(2)
cutomLL.add(3)
cutomLL.add(4)
cutomLL.add(4)
cutomLL.add(4)
cutomLL.add(7)
cutomLL.add(8)
print(cutomLL)
nthTolast(cutomLL,0)
print(cutomLL)

