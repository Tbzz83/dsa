
"""
Undirected
nodes = [
    [0,1,5],
    [0,2,5],
    [0,3,5],
    [2,1,1],
    [2,3,1]
]

read as: node 0 goes to node 1 with length 5 (and vice versa because undirected)
"""
from collections import defaultdict

def create_adj_list(nodes: list[list[int]]):
    res = defaultdict(list)
    for src, dest, ln in nodes:
        res[src].append([ln,dest])
        res[dest].append([ln,src])

    return res
