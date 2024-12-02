# FAILED: TIME LIMIT EXCEEDED
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        avg = sum(nums[0:k]) / k
        for i in range(k - 1, len(nums)):
            if sum(nums[i - k + 1:i + 1]) / k > avg:
                avg = sum(nums[i - k + 1:i + 1]) / k
                # print("avg:", avg)
        
        return avg