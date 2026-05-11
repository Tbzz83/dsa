# Given a node in a connected undirected graph, return a deep copy of the graph.
#
# Each node in the graph contains an integer value and a list of its neighbors.
#
# class Node {
#    public int val;
#    public List<Node> neighbors;
# }
#
# The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
#
# For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).
#
# The input node will always be the first node in the graph and have 1 as the value.
#
# In some way, recurse through the original graph.
# Initialize our clone to have a head node with a value of 1
# 1. Loop through cur_nodes children, clone each child.
# 2. append each child_clone to cur_clone children
# 3. set cur_node to each child, repeat 1->3.
#
# Could be done both recursively or iteratively. Let's try recursive DFS

from typing import Optional
from Intro.main import build_nodes_from_adj_map, convert_edges_list_to_adj_map, iterative_BFS_from_nodes
from Intro.node import Node 

def cloneGraph(node: Optional["Node"]) -> Optional["Node"]:
    if not node:
        return None

    seen: dict[int, Node] = {}

    new_root = Node(1)

    def dfs(cur_new: Node, cur_template: Node):
        if cur_new.val in seen:
            return
        
        seen[cur_new.val] = cur_new

        for child_node in cur_template.neighbors:
            if child_node.val in seen:
                new_child: Node = seen[child_node.val]
            else:
                new_child: Node = Node(child_node.val)

            cur_new.neighbors.append(new_child)

            dfs(new_child, child_node)

    dfs(new_root, node)

    return new_root

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
