#You are given a m×nm×n 2D grid initialized with these three possible values:
#
#    -1 - A water cell that can not be traversed.
#    0 - A treasure chest.
#    INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
#
#Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.
#
#Assume the grid can only be traversed up, down, left, or right.
#
#Modify the grid in-place.
#
#
#- We need to iterate over every land cell and calculate for each cell, the distance to the closest treasure chest.

#- if a cell already a distance set, we can use that when recursing.

#- Probably going to want to use DFS and explore all possible paths.

#- if cell == 0, treasure is in that cell. Max distance therefore is 0.
#- if a cell is touching a 0, the max distance is then set to 1.

from collections import deque

def print_grid(grid):
    for row in grid:
        print(row)

def islandsAndTreasure(grid: list[list[int]]) -> None:
    if len(grid) == 0:
        return

    ROWS, COLS = len(grid), len(grid[0])

    visited: set[tuple[int,int]] = set()
    q = deque()

    def add_land(r: int,c: int):
        if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == -1 or (r,c) in visited:
            return

        q.append((r,c))
        visited.add((r,c))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                q.append((r,c))
                visited.add((r,c))

    dist = 0

    while q:
        for _ in range(len(q)):
            r,c = q.popleft()
            grid[r][c] = dist
            add_land(r+1, c)
            add_land(r-1, c)
            add_land(r, c+1)
            add_land(r, c-1)
        dist += 1

def main():
    grid = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
#    grid = [
#        [2147483647, 0],
#        [2147483647, 2147483647],
#    ]
    islandsAndTreasure(grid)
    print_grid(grid)

if __name__ == "__main__":
    main()
