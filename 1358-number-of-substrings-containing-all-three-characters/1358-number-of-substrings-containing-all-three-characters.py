class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        last_seen = {"a": -1, "b": -1, "c": -1}
        for i in range(n):
            last_seen[s[i]] = i
            count += min(last_seen.values()) + 1
        
        return count