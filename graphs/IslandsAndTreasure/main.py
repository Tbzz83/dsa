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

from collections import deque

def print_grid(grid):
    for row in grid:
        print(row)

def islandsAndTreasure(grid: list[list[int]]) -> None:
    if len(grid) == 0:
        return

    q: deque[tuple[int, int]] = deque()
    s: set[tuple[int, int]] = set()

    ROWS, COLS = len(grid), len(grid[0])

    # Checks if coord valid ? append to q : return
    def add_to_q(coord: tuple[int, int]) -> None:
        r, c = coord

        if (r not in range(ROWS) or 
            c not in range(COLS) or
            coord in s or
            grid[r][c] == -1):
            return 

        q.append(coord)
        s.add(coord)

    # init the queue with treasure coords
    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r][c]
            if val == 0:
                q.append((r,c))
                s.add((r,c))

    distance_from_treasure: int = 0
    # Do BFS starting from treasure coords
    while q:
        q_len = len(q)

        for _ in range(q_len):
            # Only get valid coords from the q
            r, c = q.popleft()
            grid[r][c] = distance_from_treasure

            # LEFT
            add_to_q((r, c-1))
            # RIGHT
            add_to_q((r, c+1))
            # UP
            add_to_q((r-1, c))
            # DOWN
            add_to_q((r+1, c))

        distance_from_treasure += 1

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
