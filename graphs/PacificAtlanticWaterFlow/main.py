

def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:

    ROWS, COLS = len(heights), len(heights[0])
    big_res: list[list[int]] = []
    seen: dict[tuple[int, int], list[int]] = {}


    # ATLANTIC = 1
    # PACIFIC = 2
    def in_water_check(r, c) -> int:
        if r >= ROWS:
            return 2
        elif r < 0:
            return 1
        elif c >= COLS:
            return 2
        # if c < COLS
        return 1

    def dfs(r: int, c: int, parent_val: int) -> list[int]:
        res = []
        if (r not in range(ROWS)) or (c not in range(COLS)):
            res.append(in_water_check(r,c))
            return res

        val = heights[r][c]
        if parent_val < val:
            return []
        elif (r,c) in seen:
            return seen[(r,c)]

        def valid(l: list[int]):
            for num in l:
                if num == 1 and 1 not in res:
                    res.append(1)
                elif num == 2 and 2 not in res:
                    res.append(2)

        seen[(r,c)] = []

        left = dfs(r, c-1, val)
        valid(left)
        seen[(r,c)] = res

        right = dfs(r, c+1, val)
        valid(right)
        seen[(r,c)] = res

        up = dfs(r-1, c, val)
        valid(up)
        seen[(r,c)] = res

        down = dfs(r+1, c, val)
        valid(down)
        seen[(r,c)] = res

        if len(res) == 2:
            big_res.append([r,c])
        print(r,c,res)

        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r,c,heights[r][c])

    return(big_res)

def main():
#    heights = [
#  [4,2,7,3,4],
#  [7,4,6,4,7],
#  [6,3,5,3,6]
#]
    heights=[[1,1],[1,1],[1,1]]
    heights=[[10,10,10],[10,1,10],[10,10,10]]
    print(pacificAtlantic(heights))


if __name__ == "__main__":
    main()
