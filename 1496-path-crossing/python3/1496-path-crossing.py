class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0, 0)
        points = {pos}
        for d in path:
            if d == 'N':
                pos = (pos[0], pos[1]+1)
            elif d == 'E':
                pos = (pos[0] + 1, pos[1])
            elif d == 'S':
                pos = (pos[0], pos[1]-1)
            elif d == 'W':
                pos = (pos[0]-1, pos[1])
            if pos in points:
                return True
            else:
                points.add(pos)
        return False
