class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_nums = []
        for i in range(1, 10):
            prev = i
            for j in range(i + 1, 10):
                curr = prev * 10 + j
                seq_nums.append(curr)
                prev = curr
                
        return sorted([num for num in seq_nums if low <= num <= high])