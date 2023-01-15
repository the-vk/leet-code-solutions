class Solution:
    SIGNS = ['+', '-']
    DIGITS = { str(i):i for i in range(10) }
    def myAtoi(self, s: str) -> int:
        # 0 = read whitespace
        # 1 = read sign
        # 2 = read digits
        # 3 = EOF
        state = 0
        value = 0
        sign = 1
        i = 0
        while i < len(s):
            c = s[i]
            if state == 0:
                if str.isspace(c):
                    i += 1
                elif c in self.SIGNS:
                    state = 1
                elif str.isdigit(c):
                    state = 2
                else:
                    return 0
            elif state == 1:
                if c in self.SIGNS:
                    if c == '-':
                        sign = -1
                    else:
                        sign = 1
                    state = 2
                    i += 1
                elif str.isdigit(c):
                    state = 2
                else:
                    return o
            elif state == 2:
                if str.isdigit(c):
                    value = value * 10 + self.DIGITS[c]
                    i += 1
                else:
                    state = 3
            elif state == 3:
                break
        return min(max(sign*value, -pow(2, 31)), pow(2, 31) - 1)