class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
                print("profit is now:", profit)
        
        return profit