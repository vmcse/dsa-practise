class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        segments = []
        ones = 0

        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                segments.append(j - i)
                i = j
            else:
                ones += 1
                i += 1
        
        ans = 0
        for i in range(1, len(segments)):
            ans = max(ans, segments[i - 1] + segments[i])

        return ans + ones
