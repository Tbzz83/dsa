from collections import defaultdict

def countComponents(n: int, edges: list[list[int]]) -> int:
    und_map: dict[int, list[int]] = defaultdict(list)
    seen: set[int] = set()
    res: int = 0

    for v, e in edges:
        und_map[v].append(e)
        und_map[e].append(v)

    def dfs(n: int, parent: int):
        if n in seen:
            return

        seen.add(n)

        for child in und_map[n]:
            if child != parent:
                dfs(child, n)

    for node in range(n):
        if node not in seen: 
            res += 1
        dfs(node, -1)

    return res


    

    
        
def main():
    n = 3
    edges = [[0,1],[0,2]]

    n = 6
    edges = [[0,1], [1,2], [2,3], [4,5]]
    print(countComponents(n, edges))


if __name__ == "__main__":
    main()
