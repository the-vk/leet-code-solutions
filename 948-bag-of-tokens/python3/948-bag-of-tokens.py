class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
      tokens = sorted(tokens)
      max_score, score, l, r = 0, 0, 0, len(tokens) - 1
      while True:
        while l <= r and power >= tokens[l]:
          # play left token face up
          power -= tokens[l]
          score += 1
          max_score = max(max_score, score)
          l += 1
          print ('l', l, 'r', r, 'power', power, 'score', score)
        # play right token face down
        if l < r and score > 0:
          power += tokens[r]
          score -= 1
          r -= 1
          print ('l', l, 'r', r, 'power', power, 'score', score)
        else:
          break
      return max_score
