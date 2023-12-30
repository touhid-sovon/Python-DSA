# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

def listTonum(list:list):
    num = 0
    n = len(list)
    n = n-1
    for i in range(len(list)):
        num = num + list[i]*10**(n)
        n -= 1
    return num

def numToReverselist(numb):
    list = []
    while ((numb*10) / 10) >0   :
        list.append(numb % 10)
        numb = numb // 10
        #print(numb)

    return list


def addTwoNumbers(list1:list,list2:list):
    list1 = list1[::-1]
    list2 = list2[::-1]
    #print(list1,list2)
    if len(list1) ==1 and list1[0] == 0 and len(list2) ==1 and list2[0] == 0:
        return [0]
    if len(list1) ==1 and list1[0] == 0:
        return list2
    if len(list2) == 1 and list2[0] == 0:
        return list1

    num1 = listTonum(list1)
    num2 = listTonum(list2)
    #print(num1,num2)
    result = num1+ num2
    #print(result)
    return numToReverselist(result)

print(addTwoNumbers([2,4,3], [5,6,4]))

