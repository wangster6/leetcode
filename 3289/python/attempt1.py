class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dupes = [0] * 2
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    dupes[count] = nums[j]
                    count += 1
        return dupes