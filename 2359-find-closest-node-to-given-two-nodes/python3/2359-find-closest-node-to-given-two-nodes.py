class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist1 = [0] * len(edges)
        dist2 = [0] * len(edges)
        visited1 = [False] * len(edges)
        visited2 = [False] * len(edges)
        self.calc_distance(node1, edges, dist1, visited1)
        self.calc_distance(node2, edges, dist2, visited2)

        min_dist = sys.maxsize
        ans = -1
        for i in range(len(edges)):
            if visited1[i] and visited2[i] and min_dist > max(dist1[i], dist2[i]):
                min_dist = max(dist1[i], dist2[i])
                ans = i
        return ans

    def calc_distance(self, node, edges, dist, visited):
        visited[node] = True
        n = edges[node]
        if n != -1 and not visited[n]:
            dist[n] = dist[node] + 1
            self.calc_distance(n, edges, dist, visited)
