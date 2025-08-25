class Solution:
  def calculate(self, s: str) -> int:
    res, sign, num = 0, 1, 0
    stack = []

    i, n = 0, len(s)
    while i < n:
      c = s[i]
      if c.isdigit():
        num = num * 10 + int(c)
      elif c in '+-':
        res += num * sign
        num = 0
        sign = 1 if c == '+' else -1
      elif c == '(':
        stack.append(res)
        stack.append(sign)
        res, sign = 0, 1
      elif c == ')':
        res += sign * num
        num = 0
        res *= stack.pop()
        res += stack.pop()
      i += 1
    res += sign * num
    return res
        