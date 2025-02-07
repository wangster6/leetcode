class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        low, maximum = max(prices), 0
        for i in range(n):
            if prices[i] < low:
                low = prices[i]
                print("new low:", low)
            elif prices[i] - low > maximum:
                maximum = prices[i] - low
        
        return maximum