class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class Solution:
    # iterative way
    def reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def reverseList2(self,head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseList2(head.next)

        head.next.next = head
        head.next = None

        return new_head



