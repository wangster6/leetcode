class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        rtn = ""
        shorter, longer = str1, str2
        if len(str2) < len(str1):
            shorter, longer = str2, str1

        for i in range(len(shorter)):
            gcd += shorter[i]
            # print("GCD:", gcd)
            if len(shorter) % len(gcd) == 0:
                test = ""
                for j in range(int(len(shorter) / len(gcd))):
                    test += gcd
                    # print("TEST:", test)
                    if test == shorter:
                        # print("TEST = SHORTER:", test)
                        test2 = ""
                        for k in range(int(len(longer) / len(gcd))):
                            test2 += gcd
                            # print("TEST2:", test2)
                            if test2 == longer:
                                rtn = gcd
        
        return rtn
