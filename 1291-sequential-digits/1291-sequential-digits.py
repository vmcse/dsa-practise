class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            prev = i
            for j in range(i + 1, 10):
                curr = prev * 10 + j
                if low <= curr <= high:
                    ans.append(curr)
                prev = curr

        ans.sort()
        return ans