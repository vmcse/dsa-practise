from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q = deque([0])
        visited = set()

        while q:
            u = q.popleft()
            visited.add(u)
            for v in rooms[u]:
                if v not in visited:
                    q.append(v)
        
        return len(visited) == len(rooms)

        