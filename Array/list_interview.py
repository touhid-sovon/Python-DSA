# """List Interview problems """
#
# '''Finding a missing number from 1-100 but we'''
#
# # technique for creating a list from 1-100
# list1 = list(range(1,101))
# # another way by using list comprehension
# list2 = [i for i in range(1,101)]
#
# missing_list = [i for i in range(1,101) if i!=20]
#
# sum1 = int(100*101/2)
# sum2 = sum(missing_list)
#
#
# #print("The missing number is ",sum1-sum2)
#
# """ Write a program to find all the pairs whose sum is pair to a given integer"""
#
#
# n = int(input())
#
# numbers = list(map(int,input().split()))
#
# pair =[]
#
#
# for i in range(len(numbers)):
#     inside_pair = []
#     for j in range(i+1,len(numbers)):
#         if (numbers[i]+numbers[j]) == n:
#             print(numbers[i],numbers[j])
#             inside_pair.extend([numbers[i],numbers[j]])
#             pair.append(inside_pair)
#             break
#
#
#
#
# print(pair)


class Solution:
    def twoSum(self, nums: list[int], target: int):
        list1 = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    list1.extend([i, j])
                    break

        return list1

# solution1 = Solution()
# print(solution1.twoSum([2,7,11,15],9))

'''How to find maximum product of two integer where all elements are positive integers'''

import numpy as np

myArray = np.array([1,2,3,4,5,6,7,44,100,23,344,45,7,666])
myArray[::-1].sort()

# print(myArray[0],myArray[1])

'''Question 6'''
def permutation(list1,list2):
    # list1.sort()
    # list2.sort()
    set1,set2 = set(list1),set(list2)
    print(set1, set2)
    if set1 == set2:

        return "Yes"
    else:
        return "No"

list1,list2 = [6,4,9,4,5],[5,4,6,5,9,9]
# print(permutation(list1,list2)))

''' Rotate Matrix '''


















