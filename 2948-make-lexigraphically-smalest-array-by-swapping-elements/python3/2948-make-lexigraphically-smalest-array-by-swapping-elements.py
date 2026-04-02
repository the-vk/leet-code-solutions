class Solution:
  def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
    from collections import defaultdict, deque

    srt = sorted(nums)
    levels = defaultdict(deque)
    level_map = {}
    
    level = 0
    levels[level].append(srt[0])
    level_map[srt[0]] = level

    for i in range(1, len(srt)):
      v = srt[i]
      if v - levels[level][-1] > limit:
        level += 1
      levels[level].append(v)
      level_map[v] = level

    for i in range(len(nums)):
      level = level_map[nums[i]]
      nums[i] = levels[level].popleft()

    return nums
