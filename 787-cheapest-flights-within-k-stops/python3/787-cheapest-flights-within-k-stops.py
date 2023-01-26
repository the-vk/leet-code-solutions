class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = [[] for x in range(n)]
        for f,t,c in flights:
            edges[f].append((t, c))
        cost_t = [sys.maxsize] * n
        q = [(src, 0, 0, 0)]
        ans = sys.maxsize
        while len(q) > 0:
            origin, stop, cost, route = q.pop()
            
            for to, price in edges[origin]:
                cost_to = cost + price

                if to == dst:
                    ans = min(ans, cost_to)
                    continue
                bit_to = 1 << to
                if ans > cost_to and stop < k and (bit_to & route) == 0:
                    q.append((to, stop + 1, cost_to, route | bit_to))
        return ans if ans != sys.maxsize else -1
