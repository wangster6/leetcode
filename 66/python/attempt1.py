class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1          
        while digits[n] == 9:
            if n == 0:
                digits = [0] + digits
                n += 1
            digits[n] = 0
            n -= 1
        digits[n] += 1

        return digits