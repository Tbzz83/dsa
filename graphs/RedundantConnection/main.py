
from collections import defaultdict
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    und_map: dict[int, set[int]] = defaultdict(set)

    for v, e in edges:
        und_map[v].add(e)
        und_map[e].add(v)

    def non_cyclic_and_connected(node: int, parent: int, seen: set[int]) -> bool:
        if not und_map[node] or node in seen:
            return False

        seen.add(node)

        for child in und_map[node]:
            if child != parent:
                if not non_cyclic_and_connected(child, node, seen):
                    return False

        return True

    for i in range(len(edges)-1,-1,-1):
        v,e = edges[i]

        und_map[v].remove(e)
        und_map[e].remove(v)

        # Since given a guarunteed connected graph, pick any node
        if non_cyclic_and_connected(1, -1, set()):
            return [v,e]
        
        und_map[v].add(e)
        und_map[e].add(v)

    return []

def main():
    edges = [[1,2],[1,3],[3,4],[2,4]]
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    print(findRedundantConnection(edges))
    

if __name__ == "__main__":
    main()
