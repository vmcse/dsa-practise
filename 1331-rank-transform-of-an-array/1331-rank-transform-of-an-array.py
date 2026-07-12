class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr = [(arr[i], i) for i in range(n)]
        arr.sort()

        ans = [0] * n
        rank = 0
        prev = -(10 ** 9 + 1)
        for num, i in arr:
            if prev != num:
                rank += 1
                
            ans[i] = rank
            prev = num

        return ans

        