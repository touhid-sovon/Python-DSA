from base_structure import *

def returnNth(ll,n):
    leftNode = ll.head
    rightNode = ll.head

    index = 1
    while index < n:
        rightNode = rightNode.next
        index += 1


    while rightNode.next:
        rightNode = rightNode.next
        leftNode = leftNode.next


    return leftNode.value

def removeNth(ll, n):
    tempNode = Node(0)
    tempNode.next = ll.head
    left = tempNode
    right = ll.head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next
    return tempNode.next

customLL = LinkedList()
customLL.add(1)
customLL.add(2)
customLL.add(3)
customLL.add(4)
customLL.add(5)
customLL.add(6)
print(customLL)

print(returnNth(customLL,6))


removeNth(customLL, 1)

print(customLL)
