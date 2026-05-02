class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        len1 = len(str1)

        while len1 > 0:
            if len(str1) % len1 == 0  and len(str2) % len1 == 0:
                return str1[:len1]
            
            len1 -=1
        return str1[:len1]