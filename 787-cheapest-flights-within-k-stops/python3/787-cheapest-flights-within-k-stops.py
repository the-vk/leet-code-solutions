class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = [[] for x in range(n)]
        for f,t,c in flights:
            edges[f].append((t, c))
        cost_t = [sys.maxsize] * n
        q = [(src, 0)]
        stops = 0
        while q and stops <= k:
            size = len(q)
            for i in range(size):
                origin, cost = q.pop(0)
            
                for to, price in edges[origin]:
                    cost_to = cost + price
                    if cost_to > cost_t[to]:
                        continue
                    cost_t[to] = cost_to
                    q.append((to, cost_to))
            stops += 1
                    
        return cost_t[dst] if cost_t[dst] != sys.maxsize else -1

