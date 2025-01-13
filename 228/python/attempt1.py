class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        rtn = []
        start = nums[0]
        for i in range(1, len(nums)):
            # print("current:", i, "and", nums[i], "and", nums[i-1])
            if nums[i] != nums[i-1]+1:
                if start == nums[i-1]:
                    add_string = str(start)
                else:
                    add_string = str(start) + "->" + str(nums[i-1])
                # print("string:", add_string)
                rtn.append(add_string)
                start = nums[i]
            elif i == len(nums) - 1:
                add_string = str(start) + "->" + str(nums[i])
                # print("string:", add_string)
                rtn.append(add_string)
        
        if start == nums[len(nums) - 1]:
            add_string = str(start)
            # print("string:", add_string)
            rtn.append(add_string)

        return rtn