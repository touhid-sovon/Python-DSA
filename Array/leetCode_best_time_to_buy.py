''' Brute force O(n2) '''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        diff = []
        index = 0
        while(index < len(prices)):
            for i in range(index+1,len(prices)):
                if prices[index] < prices[i]:
                    diff.append(prices[i]-prices[index])
            index += 1

        if len(diff) > 0:
            return max(diff)
        else:
            return 0

# solution = Solution()
# print(solution.maxProfit([7,6,4,3,1]))


''' Optimal Solution 0(n)'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        minPurchase = prices[0]

        for price in prices:
            currentProfit = price - minPurchase
            if currentProfit > maxProfit:
                maxProfit = currentProfit
            if price < minPurchase:
                minPurchase = price

        return maxProfit
solution = Solution()
print(solution.maxProfit([7,1,4,6,1]))

