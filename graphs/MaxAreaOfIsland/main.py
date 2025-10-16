# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
#
# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
# Traverse through all coords on our grid. If we encounter land ("1"), then we can traverse starting from that point,
# and find all regions of land that come into direct contact with it.
#
# We will use a seen set, to keep track of coords that we have visited set(tuple[int])
#
# Only traverse if the current coord we are on is not in the seen set
#
# Ignore "0"
#
# Once a "1" is found, increment islands++ so long as that coord is not in the seen set
#
# Assume our grid is square
from collections import deque

def maxAreaOfIsland(grid: list[list[int]]) -> int:

    max_area: list[int] = [0]
    seen: set[tuple[int, ...]] = set()
    ROWS, COLS = len(grid), len(grid[0])

    # Point of this function is to modify seen
    def traverse(coord: tuple[int, ...]):
        area: int = 0
        q: deque[tuple[int, ...]] = deque()
        q.append(coord)
        options: list[list[int]] = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            # Unpack
            cur_r, cur_c = q.popleft()
            area += 1

            for opt in options:
                new_r, new_c = cur_r + opt[0], opt[1] + cur_c
                new_coord = (new_r, new_c)

                if (new_r in range(ROWS) and
                    new_c in range(COLS) and
                    (new_r, new_c) not in seen and
                        grid[new_r][new_c] == 1):
                    q.append(new_coord)
                    seen.add(new_coord)

        max_area[0] = max(max_area[0], area)

    for r in range(ROWS):
        for c in range(COLS):
            value: int = grid[r][c]
            if value == 0:
                continue

            coord: tuple[int, ...] = (r, c)

            if coord not in seen:
                seen.add(coord)
                traverse(coord)

    return max_area[0]

def main():
    grid = [
      [0,1,1,0,1],
      [1,0,1,0,1],
      [0,1,1,0,1],
      [0,1,0,0,1]
    ]

    print(numIslands(grid))

if __name__ == "__main__":
    main()
