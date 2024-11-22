class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        found = []
        indexes = []
        for i in range(len(s)):
            if s[i].lower() in vowel:
                found.append(s[i])
                indexes.append(i)
        
        print(found)
        print(indexes)
        found = found[::-1]
        print(found)
        rtn = list(s)
        for j in range(len(found)):
            temp = indexes[j]
            rtn[temp] = found[j]
        
        s = "".join(rtn)
        return s