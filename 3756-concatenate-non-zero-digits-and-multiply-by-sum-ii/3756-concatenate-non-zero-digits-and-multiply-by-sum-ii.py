class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        prefix_sum = [0] * n
        prefix_nonzero = [0] * n
        num_upto = [0] * n

        prefix_sum[0] = int(s[0])
        prefix_nonzero[0] = 1 if s[0] != '0' else 0
        num_upto[0] = int(s[0]) if s[0] != '0' else 0

        for i in range(1, n):
            d = int(s[i])

            prefix_sum[i] = prefix_sum[i-1] + d

            if d == 0:
                prefix_nonzero[i] = prefix_nonzero[i-1]
                num_upto[i] = num_upto[i-1]
            else:
                prefix_nonzero[i] = prefix_nonzero[i-1] + 1
                num_upto[i] = (num_upto[i-1] * 10 + d) % MOD

        pow10 = [1] * (prefix_nonzero[-1] + 1)
        for i in range(1, len(pow10)):
            pow10[i] = (pow10[i-1] * 10) % MOD

        ans = []

        for l, r in queries:
            summ = prefix_sum[r]
            if l:
                summ -= prefix_sum[l-1]

            k = prefix_nonzero[r]
            if l:
                k -= prefix_nonzero[l-1]

            x = num_upto[r]
            if l:
                x = (x - num_upto[l-1] * pow10[k]) % MOD

            ans.append((x * summ) % MOD)

        return ans