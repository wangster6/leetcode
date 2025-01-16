class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        
        if k > len(factors):
            return -1
        else:
            return factors[k - 1]