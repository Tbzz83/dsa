# You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.
# 
# Return the length of the longest strictly increasing path within matrix.
# 
# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache: dict[tuple[int, int], int] = {}
        res: int = 0

        def dfs(r, c, prev_val) -> int:
            if (r >= ROWS or r < 0 or 
                c >= COLS or c < 0 or 
                matrix[r][c] <= prev_val):
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            cur_val = matrix[r][c]
            left = dfs(r, c+1, cur_val) 
            right = dfs(r, c-1, cur_val)
            up = dfs(r-1, c, cur_val)
            down = dfs(r+1, c, cur_val)

            cache[(r,c)] = 1 + max(left, right, up, down)

            return cache[(r,c)]

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c,-1))

        return res

def main():
    matrix = [[5,5,3],[2,3,6],[1,1,1]]
    sol = Solution()

    print(sol.longestIncreasingPath(matrix))

if __name__ == "__main__":
    main()
