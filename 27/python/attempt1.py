class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] == val:
                nums[i] = None
                k += 1
        print("array:", nums)

        for j in range(n):
            if nums[j] == None:
                for l in range(j + 1, n):
                    if nums[l] != None:
                        nums[j] = nums[l]
                        nums[l] = None
                        break

        return len(nums) - k