class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 10 ** 9
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = 1
        if (1 in count):
            ones = count[1]
            if ones % 2 == 0:
                ones -= 1
            res = max(res, ones)
        
        for x in count.keys():
            if x == 1:
                continue
            
            curr = x
            curr_len = 0
            while curr <= m and count.get(curr, 0) >= 2:
                curr *= curr
                curr_len += 2
            
            if curr <= m and count.get(curr, 0) > 0:
                curr_len += 1
            else:
                curr_len -= 1
            
            res = max(res, curr_len)
        
        return res
