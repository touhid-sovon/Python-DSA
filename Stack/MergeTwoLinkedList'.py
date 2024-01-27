
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        left = list1
        right = list2
        temp = ListNode(0)
        current = temp

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            # Move the current pointer in the merged list
            current = current.next

        # If there are remaining nodes in either list, append them to the merged list
        if left:
            current.next = left
        elif right:
            current.next = right

        # Return the merged list starting from the next node of the dummy node
        return temp.next

# # Example usage
# solution = Solution()
# # Construct ListNode instances from the input lists
# list1 = ListNode(1, ListNode(4, ListNode(5)))
# list2 = ListNode(1, ListNode(2, ListNode(3)))
# result = solution.mergeTwoLists(list1, list2)
#
# # Print the result
# while result:
#     print(result.val, end=" ")
#     result = result.next

