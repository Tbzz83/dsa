from typing import DefaultDict
import heapq


class Solution():
    def createAdjList(self, tickets):
        res = DefaultDict(list)

        for src, dst in tickets:
            heapq.heappush(res[src], dst)

        return res

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        res = []
        adj_list = self.createAdjList(tickets)
        print(adj_list)

        def backtrack(node):
            if not adj_list[node]:
                res.append(node)
                return

            while adj_list[node]:
                child = heapq.heappop(adj_list[node])
                print(child)
                backtrack(child)

            res.append(node)

        backtrack('JFK')

        return res[::-1]

sol = Solution()

tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
print(sol.findItinerary(tickets))
