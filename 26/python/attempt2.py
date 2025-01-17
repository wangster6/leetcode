class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(set(nums))
        idx = 0
        history = []
        for i in range(len(nums)):
            if nums[i] not in history:
                history.append(nums[i])
                nums[idx] = nums[i]
                idx += 1
        
        return k