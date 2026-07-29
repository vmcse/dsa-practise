class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = n >> 1
        freq = [0] * 26
        for i in range(half):
            freq[ord(s[i]) - ord('a')] += 1

        def perm(rem):
            acc = 1
            for ci in range(26):
                f = freq[ci]
                if f > rem:
                    return 0
                
                acc *= comb(rem, f)
                if acc > k:
                    return acc
                
                rem -= f

            return acc
        
        left = []
        start = 0

        for i in range(half):
            selected = False
            for ci in range(26):
                if not freq[ci]:
                    continue
                
                freq[ci] -= 1
                p = perm(half - i - 1)
                if start + p >= k:
                    left.append(chr(ci + ord('a')))
                    selected = True
                    break
                
                freq[ci] += 1
                start += p
            
            if not selected:
                return ""
            
        mid = s[half] if n & 1 else ""
        left = "".join(left)

        return left + mid + left[::-1]


