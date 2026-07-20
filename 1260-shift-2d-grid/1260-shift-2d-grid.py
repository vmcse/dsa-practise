class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        for _ in range(k):
            nxt = grid[0][0]
            for i in range(n):
                for j in range(m):
                    if j == m - 1 and i < n - 1:
                        grid[i + 1][0], nxt = nxt, grid[i + 1][0]
                    elif i == n - 1 and j == m - 1:
                        grid[0][0], nxt = nxt, grid[0][0]
                    else:
                        grid[i][j + 1], nxt = nxt, grid[i][j + 1]
        
        return grid
                   
