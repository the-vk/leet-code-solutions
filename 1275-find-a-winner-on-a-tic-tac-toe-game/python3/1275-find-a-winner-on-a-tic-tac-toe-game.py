class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # False == A; True == B
        turn = False
        rows = [[] for x in range(3)]
        cols = [[] for x in range(3)]
        diag = [[] for x in range(2)]
        for r, c in moves:
            rows[r].append(turn)
            cols[c].append(turn)
            if r == c:
                diag[0].append(turn)
            if r == abs(2-c):
                diag[1].append(turn)
            turn = not turn
            for l in rows + cols + diag:
                print(l)
                if len(l) == 3 and l[0] == l[1] and l[1] == l[2]:
                    return "B" if l[0] else "A"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
        