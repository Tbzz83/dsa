"""
https://neetcode.io/problems/min-cost-to-connect-points/question?list=neetcode150
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.


So this is apparently an MST algorithm. Dijkstra's will not work because it finds the shortest path to all other nodes,
starting from some src node. See this counter-example for how MST and Dijkstras are different: https://stackoverflow.com/questions/1909281/use-dijkstras-to-find-a-minimum-spanning-tree
"""

from collections import deque
from typing import DefaultDict
import heapq


class Solution:
    def create_adj_list(self, points):
        adj_list = DefaultDict(list)
        return adj_list

    # Solve using Kruskals
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        min_heap = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                pt_1 = points[i]
                pt_2 = points[j]

                man_dist = abs(pt_1[0] - pt_2[0]) + abs(pt_1[1] - pt_2[1])

                heapq.heappush(min_heap, (man_dist,i,j))

        seen = set()

        res = 0
        while min_heap:
            if len(seen) == len(points):
                break

            dst, i, j = heapq.heappop(min_heap)
            if i in seen and j in seen:
                continue

            seen.add(i)
            seen.add(j)

            res += dst

        return res

points = [[0,0],[2,2],[3,3]]
points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
points=[[7,7],[8,0],[9,-9],[-3,4]]
points=[[2,-3],[-17,-8],[13,8],[-17,-15]]
sol = Solution()
print(sol.minCostConnectPoints(points))
