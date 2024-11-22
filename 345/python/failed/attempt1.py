class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        found = []
        indexes = []
        for i in range(len(s)):
            if s[i].lower() in vowel:
                found.append(s[i])
                indexes.append(i)
        
        # print(found)
        # print(indexes)
        found = found[::-1]
        # print(found)
        rtn = ""
        counter = 0
        for j in range(len(s)):
            if j not in indexes:
                rtn += s[j]
            else:
                rtn += found[counter]
                counter += 1

        s = rtn
        return s