class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, 1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, 1]
                
        arr = []
        l = 0
        r = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                for i in range(mid, 0, -1):
                    if nums[i] != target:
                        arr.append(i + 1)
                for j in range(mid + 1, len(nums)):
                    if nums[j] != target:
                        arr.append(i - 1)
                return arr
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, 1]