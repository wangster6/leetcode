# FAIL REASON: TIME LIMIT EXCEEDED
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max:
                    max = profit
        return max