'''
You are given a 2-D matrix grid. Each cell can have one of three possible values:

    0 representing an empty cell
    1 representing a fresh fruit
    2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
'''

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        visited = set()
        q = deque()
        t = 0
        def print_grid(grid: list[list[int]]):
            print("===")
            print(f"queue: {q}")
            for r in grid:
                print(r)
            print("===")

        def addAdjacentFruit(r,c):
            opts = [
                [r-1,c],
                [r+1,c],
                [r,c-1],
                [r,c+1],
            ]

            fruit_found = False
            for opt in opts:
                nr, nc = opt

                if nr in range(ROWS) and nc in range(COLS):
                    if grid[nr][nc] == 1 and (nr,nc) not in visited:
                        q.append((nr, nc))
                        nonlocal fresh
                        fresh -= 1
                        visited.add((nr,nc))
                        grid[nr][nc] = 2
                        fruit_found = True

            return fruit_found

        for r in range(ROWS):
            for c in range(COLS):
                fruit = grid[r][c]
                if fruit == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif fruit == 1:
                    fresh += 1
        while q:
            print_grid(grid)
            q_len = len(q)
            fruit_found = False
            for i in range(q_len):
                rotten_coord = q.popleft()
                res = addAdjacentFruit(rotten_coord[0], rotten_coord[1])
                if not fruit_found:
                    fruit_found = res

            if fruit_found:
                t += 1

        return t if fresh == 0 else -1

sol = Solution()



grid=[
    [2,1,1],
    [1,1,1],
    [0,1,2]
]

grid = [
    [1,1,0],
    [0,1,1],
    [0,1,2]
]

print(sol.orangesRotting(grid))
