# COMPLETED WITH ASSISTANCE
import string
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        new = ""
        for char in paragraph:
            if char in string.punctuation:
                char = " "
            elif char.isalpha():
                char = lower(char)
            new += char
        
        split = new.split()

        counts = {}
        for word in split:
            if word not in banned:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
        
        return max(counts, key=counts.get)