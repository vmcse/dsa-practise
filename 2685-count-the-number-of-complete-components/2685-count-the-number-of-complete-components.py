class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        root = list(range(n))

        def find(i):
            root[i] = find(root[i]) if root[i] != i else i
            return root[i]

        for u, v in edges:
            root[find(u)] = find(v)

        V, E = [[0] * n for _ in range(2)]

        for i in range(n):
            V[find(i)] += 1
            
        for u, _ in edges:
            E[find(u)] += 1

        res = 0
        for i in range(n):
            res += V[i] and E[i] == V[i] * (V[i] - 1) // 2

        return res