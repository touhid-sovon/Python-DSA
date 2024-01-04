from base_structure import *

def removeDups(ll):
    if ll.head is None:
        return
    else:
        curNode = ll.head
        visited = set([curNode.value])
        while curNode.next:
            print(curNode.next.value)
            if curNode.next.value  in visited:
                print('have duplicates')
                curNode.next = curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode = curNode.next
        print(visited)
        return ll

# cutomLL = LinkedList()
# cutomLL.add(1)
# cutomLL.add(2)
# cutomLL.add(3)
# cutomLL.add(4)
# cutomLL.add(4)
# cutomLL.add(4)
# cutomLL.add(7)
# cutomLL.add(8)
# print(cutomLL)
# removeDups(cutomLL)
# print(cutomLL)


