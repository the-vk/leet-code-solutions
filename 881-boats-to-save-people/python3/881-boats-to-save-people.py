class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
      people = sorted(people)
      l, r, boats = 0, len(people)-1, 0
      while l < r:
        boats += 1
        if people[r] + people[l] <= limit:
          l += 1
        r -= 1
      if l == r:
        boats += 1
      return boats