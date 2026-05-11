'''
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.
'''
from typing import Optional
from Intro.main import build_nodes_from_adj_map, convert_edges_list_to_adj_map, iterative_BFS_from_nodes
from Intro.node import Node 

def cloneGraph(node: Optional["Node"]) -> Optional["Node"]:
    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        copy = Node(node.val)
        old_to_new[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node) if node else None

def main():
    a: list[list[int]] = [[1,2], [2,3]] 
    adj_map = convert_edges_list_to_adj_map(a, "undirected")
    print(adj_map)

    root: Node|None = build_nodes_from_adj_map(adj_map, 1)
    if not isinstance(root, Node):
        print("FAILED")
        return
    
    new_root = cloneGraph(root)
    if new_root:
        iterative_BFS_from_nodes(new_root)

if __name__ == "__main__":
    main()

