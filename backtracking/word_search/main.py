'''
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
'''

class Solution:
    def move_opts(self, r: int, c: int) -> list[tuple[int,int]]:
        return [
            (r-1,c),
            (r+1,c),
            (r,c-1),
            (r,c+1),
        ]

    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        res: bool = False

        def backtrack(r: int, c: int, cur_word_list: list[str], seen_cells: set[tuple[int,int]]):
            cur_word_str = "".join(cur_word_list)
            if word[:len(cur_word_str)] != cur_word_str:
                return
            elif len(word) == len(cur_word_str):
                print(cur_word_str)
                nonlocal res
                res = True
                return
            elif r not in range(ROWS) or c not in range(COLS) or (r,c) in seen_cells:
                return


            # pick 
            seen_cells.add((r,c))
            cur_word_list.append(board[r][c])

            for opt in self.move_opts(r,c):
                backtrack(opt[0], opt[1], cur_word_list, seen_cells)

            cur_word_list.pop()
            seen_cells.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c,[],set())
                if res:
                    return True
        return res

sol = Solution()

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
board=[
    ["A","B","C","D"],
    ["S","A","A","T"],
    ["A","C","A","E"]
]

#board=[
#    ["A","B","C","E"],
#    ["S","F","E","S"],
#    ["A","D","E","E"]
#]
#word = "CAT"
word = "BAT"
#word = "ABCESEEEFS"
print(sol.exist(board, word))
