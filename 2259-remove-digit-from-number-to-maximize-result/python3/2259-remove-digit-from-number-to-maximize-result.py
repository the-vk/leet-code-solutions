class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i in range(len(number)):
          if number[i] == digit:
            n = int(number[:i] + number[i+1:])
            ans = max(ans, n)
        return str(ans)
