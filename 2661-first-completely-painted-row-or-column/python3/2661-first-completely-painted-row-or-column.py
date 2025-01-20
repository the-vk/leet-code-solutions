class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cols = {}
        rows = {}
        cols_j = {}
        rows_i = {}
        for i in range(m):
            if i not in rows_i:
                rows_i[i] = set()
            for j in range(n):
                if j not in cols_j:
                    cols_j[j] = set()

                v = mat[i][j]
                rows_i[i].add(v)
                cols_j[j].add(v)
                if v not in cols:
                    cols[v] = cols_j[j]
                if v not in rows:
                    rows[v] = rows_i[i]
        for i, v in enumerate(arr):
            cols[v].remove(v)
            rows[v].remove(v)
            if len(cols[v]) == 0 or len(rows[v]) == 0:
                return i
        return -1