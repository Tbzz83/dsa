"""
https://neetcode.io/problems/min-cost-to-connect-points/question?list=neetcode150
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.


So this is apparently an MST algorithm. Dijkstra's will not work because it finds the shortest path to all other nodes,
STARTING from some src node. See this counter-example for how MST and Dijkstras are different: https://stackoverflow.com/questions/1909281/use-dijkstras-to-find-a-minimum-spanning-tree


Will implement using Kruskal's algorithm which uses a UnionFind data structure (see advanced_graphs/minimum_spanning_tree)
"""

from collections import deque
from typing import DefaultDict
import heapq


class Solution:
    def find(self, uf, i) -> int:
        if uf[i] == i:
            return i

        return self.find(uf, uf[i])

    def unite(self, uf, i,j) -> list[int]:
        i_rep, j_rep = self.find(uf, i), self.find(uf, j) 

        uf[j_rep] = uf[i_rep]

        return uf


    # Solve using Kruskals
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        uf = [i for i in range(len(points))]

        sorted_edges = []
        for i, p in enumerate(points):
            for j, q in enumerate(points):
                if i == j:
                    continue

                man_dist = abs(p[0] - q[0]) + abs(p[1] - q[1])

                heapq.heappush(sorted_edges, (man_dist, i,j))

        num_groups = len(uf)
        res = 0

        while num_groups > 1:
            man_dist,i,j = heapq.heappop(sorted_edges)

            i_rep, j_rep = self.find(uf,i), self.find(uf,j)
            if i_rep == j_rep:
                continue

            self.unite(uf, i,j)
            num_groups -= 1
            res += man_dist

        return res
            



#points = [[0,0],[2,2],[3,3]]
points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
#points=[[7,7],[8,0],[9,-9],[-3,4]]
#points=[[2,-3],[-17,-8],[13,8],[-17,-15]]
sol = Solution()
print(sol.minCostConnectPoints(points))
