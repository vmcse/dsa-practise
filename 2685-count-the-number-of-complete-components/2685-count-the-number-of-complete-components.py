class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = [False] * n
        res = 0
        for i in range(n):
            if visited[i]:
                continue
            
            visited[i] = True
            q = deque([i])
            component = []

            while q:
                u = q.pop()
                component.append(u)

                for v in graph[u]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True
            
            k = len(component)
            res += 1

            for u in component:
                if len(graph[u]) != k - 1:
                    res -= 1
                    break

        return res