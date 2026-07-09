'''
https://neetcode.io/problems/network-delay-time/question?list=neetcode149

You are given a network of n directed nodes, labeled from 0 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

    ui is the source node (an integer from 0 to n)
    vi is the target node (an integer from 0 to n)
    ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).

You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

plan:

convert times map format
DFS starting from k, summing the times to travel to each node
Record visited nodes
return len(visited) == n ? time : -1
'''

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for src, dst, time in times:
            adj_list[src].append((dst,time))

        min_heap = [(0,k)]

        seen = set()
        t = 0

        while min_heap:
            distance_from_k, node = heappop(min_heap);
            if node in seen:
                continue

            t = max(t, distance_from_k)

            seen.add(node)

            for child, child_distance in adj_list[node]:
                if child in seen:
                    continue

                child_distance_from_k = child_distance + distance_from_k

                heappush(min_heap, (child_distance_from_k, child))

        return t if len(seen) == n else -1

times = [
    [1,2,1],
    [2,3,1],
    [1,4,4],
    [3,4,1]
]

n = 4
k = 1
sol = Solution()
times=[
    [1,2,1],
    [2,3,7],
    [1,3,4],
    [2,1,2]
]
n=4
k=1

print(sol.networkDelayTime(times,n,k))
