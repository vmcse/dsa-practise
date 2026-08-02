class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def dp(l, r):
            if l < r:
                return max(
                    piles[l] - dp(l + 1, r),
                    piles[r] - dp(l, r - 1)
                )
            
            return 0
        
        n = len(piles)
        return dp(0, n - 1) >= 0
        