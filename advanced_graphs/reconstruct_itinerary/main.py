'''
https://neetcode.io/problems/reconstruct-flight-path/question?list=neetcode150

You are given a list of flight tickets tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.

Each from_i and to_i consists of three uppercase English letters.

Reconstruct the itinerary in order and return it.

All of the tickets belong to someone who originally departed from "JFK". Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.

    For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].

You may assume all the tickets form at least one valid flight path.


NOTES:

- This is an undirected graph
- heappush() implicity sorts lexicographically when using strings
- the difficulty here is that we want to return an array with the path, and flights
  can return to nodes
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
        print(adj_list)
        res = []

        def dfs(node: str, q: deque) -> bool:
            res.append(node)
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj_list:
                return False

            while q:
                k, v = q.popleft()
                heappush(adj_list[k], v)

            while adj_list[node]:
                child_node = heappop(adj_list[node])

                if dfs(child_node,q):
                    return True
                res.pop()

                q.append((node, child_node))

            return False

        dfs("JFK", deque())

        return res

sol = Solution()
tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

print(sol.findItinerary(tickets))
