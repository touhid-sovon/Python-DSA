class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            if nums[left] + nums[right] == target:
                print(f'{left},{right}')
                return


solution = Solution()
# print(solution.twoSum([2,7,11,15],9))
solution.twoSum([2,7,11,15],9)