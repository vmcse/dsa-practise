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

        def dfs(city):
            s = deque([city])

            while s:
                u = s.pop()
                visited[u] = True

                for v in range(n):
                    if isConnected[u][v] and not visited[v]:
                        s.append(v)
        
        for city in range(n):
            if not visited[city]:
                dfs(city)
                count += 1
    
        return count

        




        