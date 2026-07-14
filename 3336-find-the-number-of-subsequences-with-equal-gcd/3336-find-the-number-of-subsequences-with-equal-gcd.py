class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        @cache
        def dp(i, g1, g2):
            if i == n:
                if g1 == g2:
                    return 1
                else:
                    return 0
            
            total = 0
            total = (total + dp(i + 1, g1, g2)) % MOD
            total = (total + dp(i + 1, gcd(g1, nums[i]), g2)) % MOD
            total = (total + dp(i + 1, g1, gcd(g2, nums[i]))) % MOD

            return total
        
        return (dp(0, 0, 0) - 1) % MOD
            