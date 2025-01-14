class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = len(nums) - 1
        i = 0
        while i < idx:
            # print("start nums:", nums)
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[idx]
                nums[idx] = temp
                idx -= 1
            else:
                i += 1
            # print("end nums:", nums)
        return len(nums) - nums.count(val)