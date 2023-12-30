'''Leet code : addtwoNumbers problem solution using lists'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        list1 = l1[::-1]
        list2 = l2[::-1]
        # print(list1,list2)
        if len(list1) == 1 and list1[0] == 0 and len(list2) == 1 and list2[0] == 0:
            return [0]
        if len(list1) == 1 and list1[0] == 0:
            return list2
        if len(list2) == 1 and list2[0] == 0:
            return list1

        num1 = self.listTonum(list1)
        num2 = self.listTonum(list2)
        # print(num1,num2)
        result = num1 + num2
        # print(result)
        return self.numToReverselist(result)

    def listTonum(self,list: list):
        num = 0
        n = len(list) -1
        for i in range(len(list)):
            num = num + list[i] * 10 ** (n)
            n -= 1
        return num

    def numToReverselist(self,numb):
        list = []
        while numb > 0:
            list.append(numb % 10)
            numb = numb // 10
            # print(numb)

        return list

solution1 = Solution()
print(solution1.addTwoNumbers([9,9,9,9,9,9,9,],[9,9,9,9]))