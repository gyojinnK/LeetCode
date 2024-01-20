import collections
import heapq
from pprint import pprint
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = collections.defaultdict(list)

        for nInfo in times:
            network[nInfo[0]].append((nInfo[2], nInfo[1]))

        q = []
        heapq.heappush(q, (0, k))
        dist = collections.defaultdict(int)

        while q:
            acc, curr = heapq.heappop(q)
            if curr not in dist:
                dist[curr] = acc
                for d, adj in network[curr]:
                    cost = acc + d
                    heapq.heappush(q, (cost, adj))

        return max(dist.values()) if len(dist) == n else -1