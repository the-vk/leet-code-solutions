class Solution:
  def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
    n = len(positions)
    robots = [0] * n
    # [n, pos, health, dir]
    for i in range(n):
      robots[i] = [i, positions[i], healths[i], directions[i]]
    robots = sorted(robots, key=lambda x: x[1])
    
    st = []
    for x in robots:
      if not st:
        st.append(x)
        continue
      while st and st[-1][3] == 'R' and x[3] == 'L' and st[-1][2] < x[2]:
        st.pop()
        x[2] -= 1
      if st and st[-1][3] == 'R' and x[3] == 'L' and st[-1][2] == x[2]:
        st.pop()
        continue
      if st and st[-1][3] == 'R' and x[3] == 'L' and st[-1][2] > x[2]:
        st[-1][2] -= 1
        continue
      st.append(x)

    robots = sorted(st, key=lambda x:x[0])
    return [x[2] for x in robots]
