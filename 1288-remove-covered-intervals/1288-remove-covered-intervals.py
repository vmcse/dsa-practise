class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        max_end = 0

        for l, r in intervals:
            if r > max_end:
                ans += 1
                max_end = r
                
        return ans


        