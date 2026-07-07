from collections import deque

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        stk = deque([0])
        graph1 = [[] * n for _ in range(n)]
        graph2 = [[] * n for _ in range(n)]

        for u, v in connections:
            graph1[u].append(v)

            graph2[u].append(v)
            graph2[v].append(u)
        
        visited = [False] * n
        count = 0
        while stk:
            u = stk.pop()
            visited[u] = True
            p = u
            for v in graph2[u]:
                if not visited[v]:
                    stk.append(v)
                    if p not in graph1[v]:
                        count += 1

        return count

        