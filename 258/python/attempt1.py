class Solution:
    def addDigits(self, num: int) -> int:
        string = str(num)

        while num > 9:
            sum = 0
            for i in range(len(string)):
                sum += int(string[i])
            string = str(sum)
            num = sum

        return num