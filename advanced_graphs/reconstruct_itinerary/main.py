'''
https://neetcode.io/problems/reconstruct-flight-path/question?list=neetcode150


This is an implementation of Hierholzer's algorithm for finding Euler paths/circuits

Since we could have either, when we build the adj_list we should return the start note if it's an 
Euler path, otherwise some default value
'''

from collections import defaultdict, deque
from heapq import heappop, heappush


class Solution:

    def create_adj_list(self, tickets):
        adj_list = defaultdict(list)

        for src, dst in tickets:
            heappush(adj_list[src], dst)

        return adj_list

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj_list = self.create_adj_list(tickets)
        q = deque()
        def backtrack(node: str):
            while adj_list[node]:
                backtrack(heappop(adj_list[node]))

            q.appendleft(node)

        backtrack("JFK")

        return list(q)

sol = Solution()
tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
#tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

print(sol.findItinerary(tickets))
