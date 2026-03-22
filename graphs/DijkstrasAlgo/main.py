import heapq

def dijkstra(src: int, adj: list[list[list[int]]]) -> dict[int, float]:
  paths_from_src: dict[int, float] = {v: float('inf') for v in range(len(adj))}
  paths_from_src[src] = 0

  min_heap = [(0, src)]
  visited: set[int] = set()

  while min_heap:
      distance_from_src, vertex = heapq.heappop(min_heap)

      if vertex in visited:          # skip stale entries
          continue
      visited.add(vertex)

      for v, edge in adj[vertex]:
          if v in visited:
              continue
          new_dist = distance_from_src + edge
          if new_dist < paths_from_src[v]:
              paths_from_src[v] = new_dist
              heapq.heappush(min_heap, (new_dist, v))

  return paths_from_src

def main():
    adj: list[list[list[int]]] = [[[1, 4], [2, 8]],         
            [[0, 4], [4, 6], [2,3]], 
            [[0, 8], [3, 2], [1,3]], 
            [[2, 2], [4, 10]], 
            [[1, 6], [3, 10]]]

    print(dijkstra(0, adj))




    

    

if __name__ == "__main__":
    main()
