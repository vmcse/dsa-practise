class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_grid = [0] * n
        mxi = 1
        for i in range(n):
            mxi = max(mxi, nums[i])
            prefix_grid[i] = gcd(nums[i], mxi)
        prefix_grid.sort()

        ans = 0
        l, r = 0, n - 1
        while l < r:
            ans += gcd(prefix_grid[l], prefix_grid[r])
            l += 1
            r -= 1
        
        return ans

        