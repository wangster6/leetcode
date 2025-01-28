# ASSISTED BY CHATGPT
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water, left, right = 0, 0, len(height)-1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > max_water:
                    max_water = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water