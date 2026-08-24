"""
https://neetcode.io/problems/min-cost-to-connect-points/question?list=neetcode150
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.


So this is apparently Prim's algorithm. Still struggling to understand why Dijkstra's algo won't work for this
"""

from collections import deque
from typing import DefaultDict
import heapq


class Solution:
    def print_adj_list(self, adj_list):
        for k,v in adj_list.items():
            print(k,v)
            print()

    def create_adj_list(self, points):
        adj_list = DefaultDict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                pt_1 = points[i]
                pt_2 = points[j]

                man_dist = abs(pt_1[0] - pt_2[0]) + abs(pt_1[1] - pt_2[1])

                val = (man_dist,j)

                adj_list[i].append(val)

        return adj_list

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        src = 0
        adj_list = self.create_adj_list(points)
        paths_from_src: dict[int, float] = {v: float('inf') for v in range(len(adj_list))}
        paths_from_src[src] = 0
        self.print_adj_list(adj_list)
        min_heap = []

        # dist, node
        min_heap.append((0,src))
        visited = set()
        res = 0

        while min_heap:
            dst, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)

            for dst_from_node, nxt in adj_list[node]:
                if nxt in visited:
                    continue

                new_dist = dst_from_node+dst
                res = new_dist
                if new_dist < paths_from_src[nxt]:
                    paths_from_src[nxt] = new_dist
                    heapq.heappush(min_heap, (dst_from_node+dst, nxt))

        print(paths_from_src)
        return res
                

points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
points=[[7,7],[8,0],[9,-9],[-3,4]]
sol = Solution()
print(sol.minCostConnectPoints(points))
