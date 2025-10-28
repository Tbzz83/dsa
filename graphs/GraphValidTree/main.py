from collections import defaultdict

def validTree(n: int, edges: list[list[int]]) -> bool:
    if not edges:
        return True

    adj_map: dict[int, list[int]] = defaultdict(list)

    # undirected
    def create_adj_map():
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
    create_adj_map()

    seen: set[int] = set()

    def dfs(node: int, parent: int) -> bool:
        if not adj_map[node]:
            return False


        seen.add(node)
        for child in adj_map[node]:
            if ((child != parent and child in seen) or 
                (child != parent and not dfs(child, node))):
                return False


        return True

    if not dfs(0, -1):
        return False

    if len(seen) != n:
        return False

    return True

def main():
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    #edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    #edges = [[0,1],[2,3]]

    print(validTree(n, edges))

if __name__ == "__main__":
    main()
