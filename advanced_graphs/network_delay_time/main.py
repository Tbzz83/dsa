'''
https://neetcode.io/problems/network-delay-time/question?list=neetcode150

You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

    ui is the source node (an integer from 1 to n)
    vi is the target node (an integer from 1 to n)
    ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).

You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

plan:

convert times map format
DFS starting from k, summing the times to travel to each node
Record visited nodes
return len(visited) == n ? time : -1
'''

from collections import deque
import heapq

class Solution:
    def create_adj_list(self, times: list[list[int]]):
        adj_list = {}

        for s,d,t in times:
            if s not in adj_list:
                adj_list[s] = []
            if d not in adj_list:
                adj_list[d] = []

            adj_list[s].append((d,t))

        return adj_list

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = self.create_adj_list(times)
        min_heap = [(0,k)]
        visit = set()
        t = 0

        while min_heap:
            d1, n1 = heapq.heappop(min_heap)

            if n1 in visit:
                continue

            visit.add(visit)
            t = max(t, d1)

            for n2, d2 in adj_list[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (d1+d2, n2))

        return t if len(visit) == n else -1

sol = Solution()
times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
n = 4
k = 1

print(sol.networkDelayTime(times,n,k))
