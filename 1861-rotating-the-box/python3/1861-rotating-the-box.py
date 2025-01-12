class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        out = [ [''] * m for _ in range(n) ]
        for i in range(m):
            for j in range(n):
                out[j][i] = boxGrid[m - 1 - i][j]

        for c in range(m):
            for r in range(n - 1, -1, -1):
                if out[r][c] == '#':
                    cr = r
                    for nr in range(r + 1, n):
                        if out[nr][c] in ('#', '*'):
                            break
                        if out[nr][c] == '.':
                            out[cr][c] = '.'
                            out[nr][c] = '#'
                            cr += 1                       

        return out
