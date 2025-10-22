#You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
#
#The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
#
#Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.
#
#Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.
# 
# We are going to do two 


def pacificAtlantic(heights: list[list[int]]):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    res = []

    def dfs(r: int,c:int ,visit: set[tuple[int,int]], prev_height: int):
        if ((r,c) in visit or 
            r not in range(ROWS) or
            c not in range(COLS) or 
            heights[r][c] < prev_height):
            return

        visit.add((r,c))

        dfs(r+1,c,visit,heights[r][c])
        dfs(r-1,c,visit,heights[r][c])
        dfs(r,c+1,visit,heights[r][c])
        dfs(r,c-1,visit,heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS-1, c, atl, heights[ROWS-1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS-1, atl, heights[r][COLS-1])

    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])
    return res

def main():
#    heights = [
#  [4,2,7,3,4],
#  [7,4,6,4,7],
#  [6,3,5,3,6]
#]
    heights=[[1,1],[1,1],[1,1]]
    print(pacificAtlantic(heights))


if __name__ == "__main__":
    main()
