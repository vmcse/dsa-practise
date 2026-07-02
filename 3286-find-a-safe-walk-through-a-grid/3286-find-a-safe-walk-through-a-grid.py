class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        n, m = len(grid), len(grid[0])
        
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        q = deque()
        q.append((grid[0][0], 0, 0))
        
        while q:
            cost, i, j = q.popleft()

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x >= 0 and x < n and y >= 0 and y < m:
                    new_cost = cost + grid[x][y]

                    if new_cost < dist[x][y]:
                        dist[x][y] = new_cost

                        if new_cost == cost:
                            q.appendleft((new_cost, x, y))
                        else:
                            q.append((new_cost, x, y))
        
        return dist[n-1][m-1] < health