class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        if n % 2 == 1:
            h1 = sorted(s[:n//2])
            h2 = sorted(s[n//2 + 1:], reverse=True)

            return "".join(h1 + [s[n//2]] + h2)

        h1 = sorted(s[:n//2])
        h2 = sorted(s[n//2:], reverse=True)

        return "".join(h1 + h2)
