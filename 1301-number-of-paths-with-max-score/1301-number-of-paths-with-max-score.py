class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(board)
        max_score = [[-1] * n for _ in range(n)]
        num_ways = [[0] * n for _ in range(n)]

        max_score[n - 1][n - 1] = 0
        num_ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, - 1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                if board[i][j] == 'X':
                    continue
                
                best = -1
                d = ''
                if i + 1 < n:
                    best = max(best, max_score[i + 1][j])
                if j + 1 < n:
                    best = max(best, max_score[i][j + 1])
                if i + 1 < n and j + 1 < n:
                    best = max(best, max_score[i + 1][j + 1])
                if best == -1:
                    continue
                
                ways = 0
                if i + 1 < n and max_score[i + 1][j] == best:
                    ways += num_ways[i + 1][j] 
                if j + 1 < n and max_score[i][j + 1] == best:
                    ways += num_ways[i][j + 1] 
                if j + 1 < n and i + 1 < n and max_score[i + 1][j + 1] == best:
                    ways += num_ways[i + 1][j + 1] 
                ways %= MOD
                
                curr_val = 0 if board[i][j] == 'E' else int(board[i][j])
                max_score[i][j] = best + curr_val
                num_ways[i][j] = ways
        
        return [0, 0] if max_score[0][0] == -1 else [max_score[0][0], num_ways[0][0]]