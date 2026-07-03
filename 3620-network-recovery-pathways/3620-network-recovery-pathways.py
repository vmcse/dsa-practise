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

        adj = [[] for _ in range(n)]
        max_dist = 0

        for u, v, wt in edges:
            if online[u] and online[v]:
                adj[u].append((v, wt))
                max_dist = max(max_dist, wt)

        def dijkstra(mid):
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            pq = [(0, 0)]  # (distance, node)

            while pq:
                distance, node = heapq.heappop(pq)

                if distance > dist[node]:
                    continue

                if node == n - 1:
                    return True

                for v, w in adj[node]:
                    if w < mid:
                        continue

                    new_dist = distance + w

                    if new_dist > k:
                        continue

                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))

            return False

        low, high = 0, max_dist
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if dijkstra(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
