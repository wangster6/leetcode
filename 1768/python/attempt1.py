class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = word1
        longer = word2
        if len(word1) > len(word2):
            shorter = word2
            longer = word1
        
        rtn = ""
        for i in range(len(shorter)):
            rtn += word1[i] + word2[i]
        rtn += longer[len(shorter):]

        return rtn