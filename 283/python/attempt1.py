class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            # print("nums[i]:", nums[i])
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    nums[j - 1] = nums[j]
                nums[len(nums) - 1] = 0
            # print(nums)

        return nums