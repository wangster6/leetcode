class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        curr_sum = sum(nums[0:k])
        avg = curr_sum / k
        first = True
        for i in range(k - 1, len(nums)):
            if not first:
                # print("nums[i-k]:", nums[i-k])
                # print("nums[i]:", nums[i])
                curr_sum = curr_sum - nums[i-k] + nums[i]
            else:
                first = False

            if  curr_sum / k > avg:
                avg = sum(nums[i - k + 1:i + 1]) / k
                # print("avg:", avg)
        
        return avg