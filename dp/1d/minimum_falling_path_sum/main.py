"""
https://leetcode.com/problems/minimum-falling-path-sum/description/
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

"""

class Solution:
    def getMinOptsRowBelow(self, matrix: list[list[int]], r:int, c:int, ROWS:int, COLS:int) -> int:
        opts = [(r+1,c-1),(r+1,c),(r+1,c+1)]

        res = float('inf')

        for r,c in opts:
            if (r >= 0 and r < ROWS) and (c >= 0 and c < COLS):
                if r == 1 and c == 0:
                    print(matrix[r][c])
                res = min(res,matrix[r][c])

        if res == float('inf'):
            return 0

        return int(res)

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = float('inf')

        # Iterate row by row from second to last row of matrix
        for r in range(ROWS-1,-1,-1):
            #print(matrix[r])
            for c in range(COLS):
                cell = matrix[r][c]
                matrix[r][c] = cell + self.getMinOptsRowBelow(matrix,r,c,ROWS,COLS)
                if r == 0:
                    res = min(res,matrix[r][c])

        #print(matrix)
        #if res == float
        return int(res)

sol = Solution()

matrix = [[-19,57],[-40,-5]]

matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-48]]

print(sol.minFallingPathSum(matrix))
