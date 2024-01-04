class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tally = {}
        for v in nums:
          if v not in tally:
            tally[v] = 0
          tally[v] += 1
        ans = 0
        for v, c in tally.items():
          if c == 1:
            return -1
          if (c - 4) % 3 == 0:
            ans += (c - 4) // 3 + 2
            continue
          if (c - 2) % 3 == 0:
            ans += (c - 2) // 3 + 1
            continue
          
          ans += c // 3
        return ans