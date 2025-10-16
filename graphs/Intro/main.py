from collections import defaultdict, deque


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


def queue_based_BFS(adj_map: dict[int, list[int]], root: int):
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


def convert_edges_list_to_adjacency_matrix(a: list[list[int]], n: int) -> list[list[int]]:
    adj_mtrx = [[0] * n for _ in range(n)]
    for v, e in a:
        adj_mtrx[v][e] = 1

    return adj_mtrx


def convert_edges_list_to_adjacency_map(a: list[list[int]] = [], directionality: str = "directed") -> dict[int, list[int]]:
    adj_map = defaultdict(list)

    for v, e in a:
        adj_map[v].append(e)
        if directionality == "undirected":
            adj_map[e].append(v)

    return adj_map


def main():
    n: int = 8
    a: list[list[int]] = [[0, 1], [1, 2], [0, 3], [
        3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

    adj_mtrx = convert_edges_list_to_adjacency_matrix(a, n)
    adj_map = convert_edges_list_to_adjacency_map(a)
    print("\n---Recursive DFS---")
    recursive_DFS(adj_map, 0)
    print("\n---Iterative DFS---")
    iterative_DFS(adj_map, 0)
    print("\n---Queue-based BFS---")
    queue_based_BFS(adj_map, 0)


if __name__ == "__main__":
    main()
