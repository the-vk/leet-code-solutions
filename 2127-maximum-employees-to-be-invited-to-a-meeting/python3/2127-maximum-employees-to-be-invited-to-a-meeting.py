class Solution:
    def maximumInvitations(self, favorites: List[int]) -> int:
        n = len(favorites)
        in_degree = [0] * n
        chain_lengths = [0] * n
        visited = [False] * n
        
        for fav in favorites:
            in_degree[fav] += 1
            
        q = deque(i for i in range(n) if in_degree[i] == 0)
        
        while q:
            node = q.popleft()
            visited[node] = True
            
            next_node = favorites[node]
            chain_lengths[next_node] = chain_lengths[node] + 1
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)
                
        max_cycle = total_chains = 0
        
        for i in range(n):
            if not visited[i]:
                current = i
                cycle_length = 0
                while not visited[current]:
                    visited[current] = True
                    current = favorites[current]
                    cycle_length += 1
                
                if cycle_length == 2:
                    total_chains += 2 + chain_lengths[i] + chain_lengths[favorites[i]]
                else:
                    max_cycle = max(max_cycle, cycle_length)
                    
        return max(max_cycle, total_chains)