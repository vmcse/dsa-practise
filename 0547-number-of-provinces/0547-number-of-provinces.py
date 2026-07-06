class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        parent = [i for i in range(n)]
        size = [1] * n

        def find(v):
            while parent[v] != v:
                v = parent[v]
            parent[v] = v
            return v

        def union(u, v):
            a = find(u)
            b = find(v)

            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                return True

            return False

        components = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    if union(i, j):
                        components -= 1
        
        return components


        




        