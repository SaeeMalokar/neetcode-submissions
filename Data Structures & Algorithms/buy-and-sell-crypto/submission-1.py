class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[right] - prices[left]
            if diff > profit:
                profit = diff
            if prices[right] < prices[left]:
                left = right
            right += 1 
        return profit