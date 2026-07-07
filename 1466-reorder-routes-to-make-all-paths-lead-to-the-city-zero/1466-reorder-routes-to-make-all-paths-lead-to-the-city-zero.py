from collections import deque

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        stk = deque([0])
        graph = [[] * n for _ in range(n)]
    
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(-u)
        
        visited = [False] * n
        count = 0
        while stk:
            u = stk.pop()
            visited[u] = True
            p = u
            for v in graph[u]:
                if not visited[abs(v)]:
                    stk.append(abs(v))
                    if v > 0:
                        count += 1

        return count

        