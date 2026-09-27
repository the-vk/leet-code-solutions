class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                bs = i
                be = self.match(s, bs)
                subs = list(self.reverseParentheses(s[bs+1:be]))
                subs.reverse()
                res = res + list(subs)
                i = be
            else:
                res.append(c)
            i += 1
        return ''.join(res)
    
    def match(self, s: str, start: int) -> int:
        depth = 0
        for i in range(start, len(s)):
            if s[i] == '(':
                depth += 1
            elif s[i] == ')':
                depth -= 1
                if depth == 0:
                    return i
        return -1