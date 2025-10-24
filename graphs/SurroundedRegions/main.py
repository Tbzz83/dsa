#You are given a 2-D matrix board containing 'X' and 'O' characters.
#
#If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.
#
#Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.
# 
# 1. Iterate around the border and search for 'O's. 
# 2. If 'O' encountered, DFS on that 'O' mark all of its 'O' neighbors as visited
# 3. Iterate through all other elements of the board except perimeter values
# 4. if a 'O' is encountered and is not in seen, change value to an 'X'

def solve(board: list[list[str]]) -> None: 
    ROWS, COLS = len(board), len(board[0])
    seen: set[tuple[int, int]] = set()

    def dfs(r,c):
        if ((r,c) in seen or 
            r not in range(ROWS) or
            c not in range(COLS) or 
            board[r][c] != 'O'):
            return

        seen.add((r,c))

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    # Iterate through top and bottom rows
    for c in range(COLS):
        if board[0][c] == 'O':
            dfs(0,c)

        if board[ROWS-1][c] == 'O':
            dfs(ROWS-1, c)

    # Iterate through left and right inital columns
    for r in range(ROWS):
        if board[r][0] == 'O':
            dfs(r,0)
        if board[r][COLS-1] == 'O':
            dfs(r,COLS-1)

    # Iterate through non perimeter values
    for r in range(1, ROWS-1):
        for c in range(1, COLS-1):
            if (r,c) not in seen and board[r][c] == 'O':
                board[r][c] = 'X'


def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print(row)

def main():
    board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
    solve(board)
    print_grid(board)


if __name__ == "__main__":
    main()
