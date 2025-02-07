# FAILED ATTEMPT
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n, low = len(prices), max(prices)
        arr = []

        for i in range(n):
            # print("prices[i]:", prices[i])
            if prices[i] <= low:
                low = prices[i]
            else:
                profit = prices[i] - low
                if i != n-1 and prices[i+1] < prices[i]:
                    arr.append(profit)
                    low = max(prices)
                
                if i == n-1:
                    if prices[i] > low:
                        arr.append(profit)
        
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return sum(arr)
        else:
            max1 = max(arr)
            arr.remove(max1)
            max2 = max(arr)
            return max1 + max2