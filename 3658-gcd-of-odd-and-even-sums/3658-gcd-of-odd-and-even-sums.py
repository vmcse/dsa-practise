class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_even = n * (n + 1)
        sum_odd = n * n

        return gcd(sum_odd, sum_even)
