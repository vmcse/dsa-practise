class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0 
        for pattern in patterns:
            if word.find(pattern) != -1:
                count += 1
        
        return count