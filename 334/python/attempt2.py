class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 2:
            return False

        if max(nums) - min(nums) < 2:
            return False

        for i in range(len(nums)):
            if nums[i] != max(nums):
                # print("CP1")
                for j in range(len(nums) - 1, i + 1, -1):
                    if nums[j] > nums[i]:
                        # print("CP2")
                        for k in range(i + 1, j):
                            # print("k:", k)
                            if nums[i] < nums[k] < nums[j]:
                                return True
        return False