class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        open_cnt = 0
        closed_cnt = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                open_cnt += 1
            else:
                open_cnt -= 1
            if open_cnt < 0:
                return False

        for i in range(n-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                closed_cnt += 1
            else:
                closed_cnt -= 1
            if closed_cnt < 0:
                return False
        return True
