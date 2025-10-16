from collections import defaultdict, deque
from collections.abc import Callable
from typing import Optional
from .node import Node

def recursive_DFS(adj_map: dict[int, list[int]], root: int):
    seen: set[int] = set()
    seen.add(root)

    def dfs(node: int):
        print(node)

        for node in adj_map[node]:
            if node not in seen:
                seen.add(node)
                dfs(node)

    dfs(root)

def iterative_DFS(adj_map: dict[int, list[int]], root: int):
    seen: set[int] = set()
    stack: list[int] = []

    stack.append(root)
    seen.add(root)

    while stack:
        popped = stack.pop()

        print(popped)

        for node in adj_map[popped]:
            if node not in seen:
                seen.add(node)
                stack.append(node)

# 'action' is a function that will be performed on each popped element from the queue
# as the BFS takes place
def queue_based_BFS(adj_map: dict[int, list[int]], root: int, func: Optional[Callable] = None):
    q: deque[int] = deque()
    seen = set()
    seen.add(root)
    q.append(root)

    while q:
        q_len = len(q)

        for _ in range(q_len):

            popped = q.popleft()
            print(popped)

            for node in adj_map[popped]:
                if node not in seen:
                    q.append(node)
                    seen.add(node)

def convert_edges_list_to_adj_mtrx(a: list[list[int]], n: int) -> list[list[int]]:
    adj_mtrx = [[0] * (n) for _ in range(n)]
    for v, e in a:
        print(adj_mtrx)
        print(v,e)
        adj_mtrx[v][e] = 1

    return adj_mtrx

# Options for directionality are "directed" or "undirected"
def convert_edges_list_to_adj_map(a: list[list[int]] = [], directionality: str = "directed") -> dict[int, list[int]]:
    adj_map = defaultdict(list)

    for v, e in a:
        adj_map[v].append(e)
        if directionality == "undirected":
            adj_map[e].append(v)

    return adj_map

def build_nodes_from_adj_map(adj_map: dict[int, list[int]], root: int) -> Optional["Node"]:
    if not adj_map:
        return None

    root_node: Node = Node(root)
    seen: dict[int, Node] = {}
    seen[root] = root_node
    q: deque[int] = deque()
    q.append(root)

    while q:
        popped = q.popleft()
        cur = seen[popped]

        for child in adj_map[popped]:
            if child not in seen:
                child_node: Node = Node(child)
                q.append(child)
                seen[child] = child_node
            else:
                child_node: Node = seen[child]

            cur.neighbors.append(child_node)

    return root_node

def iterative_BFS_from_nodes(root: Node):
    q: deque[Node] = deque()
    seen: set[Node] = set()

    q.append(root)
    seen.add(root)  # Mark root as seen immediately!

    while q:
        q_len = len(q)

        for _ in range(q_len):
            node = q.popleft()

            print("parent", node.val)
            print(f"children of {node.val}")
            for child in node.neighbors:
                print(child.val)
                if child not in seen:
                    q.append(child)
                    seen.add(child)

        print(" ---")
 
def main():
    n: int = 8
    a: list[list[int]] = [[0, 1], [1, 2], [0, 3], [
        3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

    adj_mtrx = convert_edges_list_to_adj_mtrx(a, n)
    adj_map = convert_edges_list_to_adj_map(a)
    print("\n---Recursive DFS---")
    recursive_DFS(adj_map, 0)
    print("\n---Iterative DFS---")
    iterative_DFS(adj_map, 0)
    print("\n---Queue-based BFS---")
    queue_based_BFS(adj_map, 0)

if __name__ == "__main__":
    main()
