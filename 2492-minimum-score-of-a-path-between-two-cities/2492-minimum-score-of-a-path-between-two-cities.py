from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        q = deque([1])
        visited = set()

        graph = {i: [] * n for i in range(1, n + 1)}
        for road in roads:
            a, b, dist = road[0], road[1], road[2]
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        score = 10 ** 4

        while q:
            u = q.popleft()
            visited.add(u)

            for v, dist in graph[u]:
                if v not in visited:
                    score = min(score, dist)
                    q.append(v)

        return score