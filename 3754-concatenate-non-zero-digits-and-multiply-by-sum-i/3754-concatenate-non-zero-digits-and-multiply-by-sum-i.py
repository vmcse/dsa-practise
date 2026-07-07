import re

class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        non_zero = [i for i in str(n) if i != '0']
        x = ''.join(non_zero)
        x = int(x) if x else 0
        s = sum([int(i) for i in non_zero if i])

        return x * s
        