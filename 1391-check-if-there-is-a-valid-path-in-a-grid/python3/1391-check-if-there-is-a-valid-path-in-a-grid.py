class Solution:
  def hasValidPath(self, grid: List[List[int]]) -> bool:
    M = len(grid)
    N = len(grid[0])
    TARGET = (M-1, N-1)
    U = 0
    R = 1
    D = 2
    L = 3
    dirs = [
      [-1, 0],
      [0, 1],
      [1, 0],
      [0, -1]
    ]

    connectivity_map = {
      1: [
        set(),
        set([1, 3, 5]),
        set(),
        set([1, 4, 6])
      ],
      2: [
        set([2, 3, 4]),
        set(),
        set([2, 5, 6]),
        set()
      ],
      3: [
        set(),
        set(),
        set([2, 5, 6]),
        set([1, 4, 6])
      ],
      4: [
        set(),
        set([1, 3, 5]),
        set([2, 5, 6]),
        set()
      ],
      5: [
        set([2, 3, 4]),
        set(),
        set(),
        set([1, 4, 6])
      ],
      6: [
        set([2, 3, 4]),
        set([1, 3, 5]),
        set(),
        set()
      ]
    }

    def is_traversable(f, t, dir):
      #print(f, t, dir)
      if t[0] < 0 or t[0] >= M:
        return False
      if t[1] < 0 or t[1] >= N:
        return False
      ft = grid[f[0]][f[1]]
      tt = grid[t[0]][t[1]]
      fs = connectivity_map[ft][dir]
      ts = connectivity_map[tt][(dir + 2) % len(dirs)]
      #print(fs, ts)
      return fs & ts

    seen = set()
    q = deque([(0, 0)])
    while q:
      #print(q)
      f = q.popleft()
      if TARGET == f:
        return True
      if f in seen:
        continue
      seen.add(f)
      for dir, d in enumerate(dirs):
        ti = f[0] + d[0]
        tj = f[1] + d[1]
        t = (ti, tj)
        if is_traversable(f, t, dir):
          q.append(t)

    return False
