"""
Steps for using Kruskal's algorithm to find a minimum-spanning-tree

1. Sort edges by ascending edge weight

2. Walk through the sorted edges and look a tht eht two nodes the edge belongs to. 
   if the nodes are already unified (in the same group) then we don't include this edge. 
   otherwise, we incldude it and unify the nodes (merge the groups)

3. The algorithm terminates when every edge has been processed or all the vertices have been unified (only one group remains)


We need to implement this using a Union-Find data structure (disjoint set): https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

"""
from advanced_graphs.minimum_spanning_tree.utils import create_adj_list
import heapq

class Kruskals:
    def create_min_heap_adj_list(self) -> list[tuple[int]]:
        """
        Returns array formatted using heapq min heap
        """
        res = []
        for src, targets in self.adj_list.items():
            for ln, target in targets:
                heapq.heappush(res,(ln,src,target))

        return res

    def __init__(self, nodes) -> None:
        self.adj_list = create_adj_list(nodes)

    def compute(self):
        min_heap_adj_list = self.create_min_heap_adj_list()
        print(min_heap_adj_list)

class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))

    def find(self, i):
        if self.parent[i]
        

# Undirected
nodes = [
    [0,1,5],
    [0,2,5],
    [0,3,5],
    [2,1,1],
    [2,3,1]
]

#alg = Kruskals(nodes)
#alg.compute()

