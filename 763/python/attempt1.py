# COMPLETED WITH ASSISTANCE FROM SOLUTION
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        end_occur = {char: idx for idx, char in enumerate(s)}
        
        lengths = []
        left = 0
        right = 0
        for idx, char in enumerate(s):
            right = max(right, end_occur[char])

            if idx == right:
                lengths.append(right - left + 1)
                left = right + 1
                right = right + 1
        
        return lengths