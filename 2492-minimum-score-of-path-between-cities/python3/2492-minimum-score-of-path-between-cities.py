class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w
        
        min_score = float('inf')
        visit_vector = [0] * 1563
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                seg = (adj - 1) // 64
                bit = 1 << ((adj-1) % 64)
                visited = visit_vector[seg] & bit
                if visited == 0:
                    queue.append(adj)
                    visit_vector[seg] |= bit
                min_score = min(min_score, score)
                
        return min_score