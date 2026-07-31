class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        ans = 0
        for i, f in enumerate(sorted(freq.values(), reverse=True)):
            ans += ((i >> 3) + 1) * f
            print(ans)
        
        return ans
        