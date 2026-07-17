class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)

        arr = [0] * (m + 1)
        for n in nums:
            arr[n] += 1
        
        for i in range(1, m + 1):
            for j in range(i * 2, m + 1, i):
                arr[i] += arr[j]
        
        for i in range(1, m + 1):
            arr[i] = arr[i] * (arr[i] - 1) // 2
        
        for i in range(m, 0, -1):
            for j in range(i * 2, m + 1, i):
                arr[i] -= arr[j]
        
        for i in range(1, m + 1):
            arr[i] += arr[i - 1]
        
        return [bisect.bisect_left(arr, q + 1) for q in queries]


        