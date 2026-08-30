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
from advanced_graphs.minimum_spanning_tree.union_find import UnionFind
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
        print(self.adj_list)
        self.num_nodes = len(self.adj_list.keys())

    def compute(self):
        min_heap_adj_list = self.create_min_heap_adj_list()
        uf = UnionFind(self.num_nodes)

        num_groups = self.num_nodes
        res = 0

        while num_groups > 1 and len(min_heap_adj_list) > 0:
            ln, src, target = heapq.heappop(min_heap_adj_list)
            
            src_rep, target_rep = uf.find(src), uf.find(target)
            if src_rep == target_rep:
                continue

            uf.unite(src_rep, target_rep)
            num_groups -= 1
            res += ln

        return res


# src, dest, length
nodes = [
    [0,1,5],
    [0,2,5],
    [0,3,5],
    [2,1,1],
    [2,3,1]
]

alg = Kruskals(nodes)
print(alg.compute())
