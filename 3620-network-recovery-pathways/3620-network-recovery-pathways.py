import heapq
class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        graph = [[] for _ in range(n)]
        low, high = float('inf'), 0

        for u, v, wt in edges:
            if online[u] and online[v]:
                graph[u].append((v, wt))
                high = max(high, wt)
                low = min(low, wt)

        def dijkstra(mid):
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            pq = [(0, 0)]  # (distance, node)

            while pq:
                d, u = heapq.heappop(pq)

                if d > dist[u]:
                    continue

                if u == n - 1:
                    return True

                for v, wt in graph[u]:
                    if wt < mid:
                        continue

                    new_dist = d + wt
                    if new_dist > k:
                        continue

                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))

            return False

        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if dijkstra(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
