from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def bfs(city):
            q = deque([city])

            while q:
                u = q.popleft()
                visited[u] = True

                for v in range(n):
                    if isConnected[u][v] and not visited[v]:
                        q.append(v)
        
        for city in range(n):
            if not visited[city]:
                bfs(city)
                count += 1
    
        return count

        




        