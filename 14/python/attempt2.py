class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        shortest = strs[0]
        for str in strs:
            if len(str) < len(shortest):
                shortest = str
        idx = strs.index(shortest)
        strs[idx] = strs[0]
        strs[0] = shortest

        lcp = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return lcp
            lcp += strs[0][i]
        return lcp