class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent = [i for i in range(n)] 
        size = [0] * n

        def find(u):
            root = u

            while root != parent[root]:
                root = parent[root]

            while u != root:
                nxt = parent[u]
                parent[u] = root
                u = nxt

            return root
        
        def union(u, v):
            a, b = find(u), find(v)

            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                
                parent[b] = a
                size[a] += size[b]
        
            
        for i in range(n - 1):
                if abs(nums[i] - nums[i + 1]) <= maxDiff:
                    union(i, i + 1)
        ans = []

        for u, v in queries:
            ans.append(find(u) == find(v))

        return ans
        