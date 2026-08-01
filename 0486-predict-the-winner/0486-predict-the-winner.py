class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def dp(l, r):
            if l == r:
                return nums[l]
            
            return max(nums[l] - dp(l + 1, r), nums[r] - dp(l, r - 1))
        
        n = len(nums)
        return dp(0, n - 1) >= 0


        