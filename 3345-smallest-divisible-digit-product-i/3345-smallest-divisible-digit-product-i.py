class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            p = 1
            for d in str(i):
                p *= int(d)
            
            if p % t == 0:
                return i

            i += 1
        