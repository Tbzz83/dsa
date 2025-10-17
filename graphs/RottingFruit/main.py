#You are given a 2-D matrix grid. Each cell can have one of three possible values:
#
#    0 representing an empty cell
#    1 representing a fresh fruit
#    2 representing a rotten fruit
#
#Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
#
#Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Use BFS 
#
# Start from rotting fruits first. 
# 1. Initialize global vars (q, seen set, time = 0)
# 2. Find all rotting fruit, add to q as initialization step
# 3. pop rotting fruits. add neighbors to q (use validate_and_add func to check neighbor coords are in-bound )
# 4. time ++ 
# 5. Continue until queue empty

from collections import deque

from IslandsAndTreasure.main import print_grid

def orangesRotting(grid: list[list[int]]) -> int:
    if len(grid) == 0:
        return 0

    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

    ROWS, COLS = len(grid), len(grid[0])
    q: deque[tuple[int, int]] = deque()
    s: set[tuple[int, int]] = set()

    # Contains all the coordinates of the fresh fruit
    fresh_coords: set[tuple[int, int]] = set()
    time: int = -1

    # init our q with rotten fruit
    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r][c]

            if val == ROTTEN:
                q.append((r,c))
                s.add((r,c))

            elif val == FRESH:
                fresh_coords.add((r,c))

    def validate_and_add(r: int, c: int):
        if (r not in range(ROWS) or
            c not in range(COLS) or 
            (r,c) in s or
            grid[r][c] == EMPTY):
            return

        fresh_coords.remove((r,c))
        q.append((r,c))
        s.add((r,c))

    while q:
        q_len: int = len(q)

        for _ in range(q_len):
            r, c = q.popleft()
            grid[r][c] = 2

            validate_and_add(r,c+1)
            validate_and_add(r,c-1)
            validate_and_add(r+1,c)
            validate_and_add(r-1,c)

        time += 1
        print_grid(grid)
        print(time)
        print("---")

    if time == -1: time = 0
    return time if len(fresh_coords) == 0 else -1

def main():
    grid = [[1,1,0],[0,1,1],[0,1,2]]

    print(orangesRotting(grid))

if __name__ == "__main__":
    main()
