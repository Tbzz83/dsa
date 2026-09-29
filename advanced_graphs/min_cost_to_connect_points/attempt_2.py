"""
https://neetcode.io/problems/min-cost-to-connect-points/question?list=neetcode150
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.


So this is apparently an MST algorithm. Dijkstra's will not work because it finds the shortest path to all other nodes,
STARTING from some src node. See this counter-example for how MST and Dijkstras are different: https://stackoverflow.com/questions/1909281/use-dijkstras-to-find-a-minimum-spanning-tree


Will implement using Kruskal's algorithm which uses a UnionFind data structure (see advanced_graphs/minimum_spanning_tree)
"""

from heapq import heappop, heappush


class Solution:
    def create_sorted_man_dists(self, points):
        res = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                a,b = points[i], points[j]
                man_dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
                heappush(res,(man_dist,i,j))

        return res

    def find(self, uf, i):
        if i == uf[i]:
            return i

        return self.find(uf, uf[i])

    def unite(self, uf, i, j):
        i_rep, j_rep = self.find(uf,i), self.find(uf,j)

        assert i_rep == uf[i_rep]
        assert j_rep == uf[j_rep]

        uf[j_rep] = i_rep

        return uf

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        min_heap = self.create_sorted_man_dists(points)
        uf = [i for i in range(len(points))]
        num_groups = len(points)
        
        res = 0

        while num_groups > 1:
            d, i, j = heappop(min_heap)

            if self.find(uf,i) != self.find(uf,j):
                self.unite(uf,i,j)
                num_groups -= 1
                res += d

        return res

sol = Solution()
points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

print(sol.minCostConnectPoints(points))
