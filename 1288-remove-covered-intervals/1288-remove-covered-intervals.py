class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        def is_covered(interval, intervals, covered):
            a, b = interval
            for i in range(len(intervals)):
                c, d = intervals[i]
                if (c, d) in covered or (a == c and b == d):
                    continue

                if c <= a and b <= d:
                    return True
            
            return False

        n = len(intervals)
        ans = n
        covered = set()

        for interval in intervals:
            if is_covered(interval, intervals, covered):
                ans -= 1
                covered.add((interval[0], interval[1]))

        return ans


        