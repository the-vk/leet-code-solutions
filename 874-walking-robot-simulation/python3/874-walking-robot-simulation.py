class Solution:
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    dirs = [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0]
    ]
    n = len(dirs)

    d = 0
    p = [0, 0]
    answ = 0

    obst = set([(x, y) for x, y in obstacles])

    def normalize_d(d):
      if d < 0:
        d = n + d
      else:
        d = d % n
      return d

    for c in commands:
      if c == -2:
        d -= 1
        d = normalize_d(d)
      elif c == -1:
        d += 1
        d = normalize_d(d)
      else:
        np = [p[0], p[1]]
        for k in range(1, c+1):
          nx = np[0] + dirs[d][0]
          ny = np[1] + dirs[d][1]
          if (nx, ny) in obst:
            break
          np = [nx, ny]
        p = np
        answ = max(answ, p[0] ** 2 + p[1] ** 2)
      print(c, p, d)

    return answ
