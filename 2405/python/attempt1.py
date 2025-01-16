class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn = []
        string = ""
        for char in s:
            if char in string:
                rtn.append(string)
                # print("string appended")
                string = ""
                # print("rtn:", rtn)
            
            if not char in string:
                string = string + str(char)
                # print("string:", string)
        rtn.append(string)

        return len(rtn)