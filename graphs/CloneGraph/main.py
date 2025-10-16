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
from ..Intro.main import iterative_DFS


class Node:
    def __init__(self, val=0, neighbors: list[Optional["Node"]] = []) -> None:
        self.val = val
        self.neighbors: list[Node | None] = neighbors if neighbors else []


def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
    pass


def main():
    a: list[list[int]] = [[0, 1], [1, 2], [0, 3], [
        3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
    pass


if __name__ == "__main__":
    main()
