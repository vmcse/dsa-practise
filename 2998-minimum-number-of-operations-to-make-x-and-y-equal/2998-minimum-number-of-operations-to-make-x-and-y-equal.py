class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        q = deque([(x, 0)])
        visited = {x}

        while q:
            u, dist = q.popleft()
            if u == y:
                return dist
            neighbors = [u + 1, u - 1]
            if u % 11 == 0:
                neighbors.append(u / 11)
            if u % 5 == 0:
                neighbors.append(u / 5)
            
            for v in neighbors:
                if v not in visited:
                    visited.add(v)
                    q.append((v, dist + 1))
        
        