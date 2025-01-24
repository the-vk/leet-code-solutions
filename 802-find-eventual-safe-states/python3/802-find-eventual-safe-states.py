class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = set()
        not_safe = set()
        
        seen = set()
        def walk(i: int) -> bool:
            if i in not_safe:
                return False
            if i in safe:
                return True
            if i in seen:
                not_safe.add(i)
                return False
            if len(graph[i]) == 0:
                safe.add(i)
                return True
            seen.add(i)
            s = True
            for x in graph[i]:
                s = s and walk(x)
            seen.remove(i)
            if s:
                safe.add(i)
            return s

        for i in range(n):
            if walk(i):
                safe.add(i)

        return sorted([x for x in safe])
        