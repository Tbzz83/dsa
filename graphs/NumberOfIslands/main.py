'''
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water). 

'''

import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        res = 0
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])


        def bfs(r: int,c: int):
            q = collections.deque()
            q.appendleft((r,c))

            while len(q) > 0:
                coord: tuple[int,int] = q.popleft()
                cur_r, cur_c = coord[0], coord[1]
                opts = [(cur_r,cur_c-1),
                        (cur_r,cur_c+1),
                        (cur_r-1,cur_c),
                        (cur_r+1,cur_c)]

                for opt in opts:
                    opt_r, opt_c = opt[0], opt[1]
                    if opt_r in range(NUM_ROWS) and opt_c in range(NUM_COLS) and grid[opt_r][opt_c] == "1" and (opt_r,opt_c) not in visited:
                        visited.add((opt_r,opt_c))
                        q.appendleft((opt_r,opt_c))


        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                val = grid[r][c]

                if val == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    res += 1
                    bfs(r,c)
                else:
                    continue
        return res

def main():
    grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]
    grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

    sol = Solution()
    print(sol.numIslands(grid))



if __name__ == "__main__":
    main()
