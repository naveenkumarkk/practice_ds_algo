import numpy  as np

class Solution:
    def myAtoi(self, s: str) -> int:
        s = str.strip(s)
        if len(s) == 0:
            return 0
        result = 0
        if (str.isnumeric(s[1]) or s[1]=='-'):
            for i in range(len(s)):
                if str.isnumeric(s[i]):
                    result = max(result * 10 + int(s[i]),1)
                else:
                    return result


        return 0

            
