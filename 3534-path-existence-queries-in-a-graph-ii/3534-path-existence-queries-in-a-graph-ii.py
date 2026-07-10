class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort()
        
        ntoi = {}
        for i, (v, node) in enumerate(nums):
            ntoi[node] = i

        maxjumps = [0] * n
        for i, (v, node) in enumerate(nums):
            nxt = bisect.bisect_left(nums, (v + maxDiff, inf)) - 1
            maxjumps[i] = nxt
        
        LOG = n.bit_length()
        up = [maxjumps]

        for _ in range(1, LOG):
            last = up[-1]
            up.append([last[last[i]] for i in range(n)])
        
        ans = []
        for u, v in queries:
            u = ntoi[u]
            v = ntoi[v]

            if u == v:
                ans.append(0)
                continue
            
            if u > v:
                u, v = v, u

            curr = u
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][curr] < v:
                    curr = up[k][curr]
                    jumps += 1 << k
            
            if maxjumps[curr] >= v:
                ans.append(jumps + 1)
            else:
                ans.append(-1)

        return ans
