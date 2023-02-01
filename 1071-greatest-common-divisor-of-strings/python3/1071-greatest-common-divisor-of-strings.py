class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        m = 1
        while m <= len(str2):
            if len(str2) % m == 0:
                d = str2[0:len(str2) // m]
                if self.isDivisor(str1, d) and self.isDivisor(str2, d):
                    return d
            m += 1
        return ""

    def isDivisor(self, str1, str2):
        return len(str1) % len(str2) == 0 and str1 == (str2 * (len(str1) // len(str2)))
