class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        tempHash = {}

        # build the hash table
        for i in range(n):
            tempHash[nums[i]]=i

        # finding the remainder
        for i in range(n):
            remainder = target - nums[i]

            if remainder in tempHash and tempHash[remainder] != i :
                return [i,tempHash[remainder]]

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        tempHash = {}

        for i in range(n):
            remainder = target - nums[i]
            if remainder in tempHash:
                return [tempHash[remainder],i]
            tempHash[nums[i]] = i



solution = Solution2()
print(solution.twoSum([3,2,4],6))