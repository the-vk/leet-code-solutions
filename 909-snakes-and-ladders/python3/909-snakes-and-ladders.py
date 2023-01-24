class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = [(1, 0)]
        cost = {1: 0}
        n = len(board)
        nsq = n * n
        while len(queue) > 0:
            p, c = queue.pop(0)
            for i in range(p+1, min(p + 7, nsq+1)):
                x, y = self.p_to_x_y(i, n)
                d = i if board[y][x] == -1 else board[y][x]
                if d == nsq:
                    return c + 1
                if d in cost and cost[d] < c + 1:
                    continue
                queue.append((d, c + 1))
                cost[d] = c + 1
        return -1

    def p_to_x_y(self, p, n):
        y = n - ((p-1)//n) - 1
        x = (n*2 - (p % (n*2))) % (n*2) if (n - y) % 2 == 0 else p % (n*2) - 1
        return (x, y)