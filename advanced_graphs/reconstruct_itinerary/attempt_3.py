'''
https://neetcode.io/problems/reconstruct-flight-path/question?list=neetcode150


This is an implementation of Hierholzer's algorithm for finding Euler paths/circuits

Since we could have either, when we build the adj_list we should return the start note if it's an 
Euler path, otherwise some default value


You are given a list of flight tickets tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.

Each from_i and to_i consists of three uppercase English letters.

Reconstruct the itinerary in order and return it.

All of the tickets belong to someone who originally departed from "JFK". Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.

    For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].

You may assume all the tickets form at least one valid flight path.
'''

from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def createAdjList(self, tickets):
        adj_list = defaultdict(list)

        for src, dst in tickets:
            heappush(adj_list[src], dst)

        return adj_list

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj_list = self.createAdjList(tickets)
        res = []

        def recurse(node: str):
            while adj_list[node]:
                recurse(heappop(adj_list[node]))

            res.append(node)

        recurse("JFK")
        return res[::-1]
        

sol = Solution()
tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

print(sol.findItinerary(tickets))
