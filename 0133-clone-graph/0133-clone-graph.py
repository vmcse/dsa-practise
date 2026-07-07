"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
            
        q = deque([node])
        cloned = {node: Node(node.val)}
        
        while q:
            u = q.popleft()

            for v in u.neighbors:
                if v not in cloned:
                    cloned[v] = Node(v.val)
                    q.append(v)
                
                cloned[u].neighbors.append(cloned[v])
        
        return cloned[node]
        


        