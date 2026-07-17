'''
Making sure I can still figure out this question on my own since it is a staple for graph problems to come.

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
import heapq

class Solution:
    def create_adj_list(self, times: list[list[int]]):
        adj_list = defaultdict(list)
        for s, d, t in times:
            adj_list[s].append((t,d))

        return adj_list

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        min_heap = []
        adj_list = self.create_adj_list(times)
        heapq.heappush(min_heap, (0,k))
        seen = set()
        t = 0

        while min_heap:
            dist_from_k, node = heapq.heappop(min_heap)
            if node in seen:
                continue
            seen.add(node)
            t = dist_from_k

            for child_dist_from_node, child_node in adj_list[node]:
                if child_node in seen:
                    continue
                heapq.heappush(min_heap, (child_dist_from_node + dist_from_k, child_node))

        return t if len(seen) == n else -1

sol = Solution()


times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
n = 4
k = 1

print(sol.networkDelayTime(times,n,k))
