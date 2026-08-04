class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        start, end = nums[0], nums[-1]

        def find(i):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                
                if nums[mid] == i:
                    return True
                if i > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        ans = []
        for i in range(start, end + 1):
            if not find(i):
                ans.append(i)
        
        return ans
