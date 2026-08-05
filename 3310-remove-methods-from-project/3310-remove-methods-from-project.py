class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited = [False] * n
        visited[k] = True
        stk = deque([k])

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        while stk:
            u = stk.pop()

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stk.append(v)
        
        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))
        
        return [i for i in range(n) if not visited[i]]

        
