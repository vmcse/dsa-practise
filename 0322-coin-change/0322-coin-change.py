class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = float('inf')
        dp = [inf] * (amount + 1)
        dp[0] = 0
        n = len(coins)
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] != inf:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != inf else -1

        