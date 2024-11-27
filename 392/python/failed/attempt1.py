class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for i in range(len(s)):
            try:
                # print("t[ptr + 1:].index(s[i]):", t[ptr + 1:].index(s[i]))
                # print("ptr:", ptr)
                # print("t[ptr:]:", t[ptr:])
                ptr = t[ptr:].index(s[i])
                # print("t:", t)
                t = t[ptr + 1:]
            except Exception as e:
                # print("THE EXCEPTION:", e)
                return False
        return True
            
                    