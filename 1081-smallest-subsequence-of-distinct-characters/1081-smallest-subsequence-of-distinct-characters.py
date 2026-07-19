class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        last_seen = {}

        for i, c in enumerate(s):
            last_seen[c] = i
        
        ans = []

        for i, c in enumerate(s):
            if c in ans:
                continue
            
            while ans and c < ans[-1] and i < last_seen[ans[-1]]:
                ans.pop()
            ans.append(c)

        return "".join(ans)