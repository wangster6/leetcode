# TIME - 25:03
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[i] = suffix[i-1] * nums[len(nums)-i]
        
        suffix = suffix[::-1]
        # print(prefix)
        # print(suffix)

        return [prefix[i] * suffix[i] for i in range(len(nums))]