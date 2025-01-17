## ASSISTED WITH GOOGLE
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        max = nums[0]
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
            if counts[num] > counts[max]:
                max = num
        
        return max