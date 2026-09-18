"""
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.


SOLUTION:
lesson here is to not keep trying the same thing over and over again. I initially attempted building the trie based on the board, but you build it based 
on the words. 

Then you can easily do your DFS starting from each c in board, and basically 
"""


class Node:
    def __init__(self) -> None:
        self.is_word = False
        self.children = {}

    def __repr__(self) -> str:
        return f"{self.children}"

    def add_word(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()

        root = Node()

        for word in words:
            root.add_word(word)


        seen = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r: int, c: int, cur: Node, cur_str: str):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] not in cur.children or (r,c) in seen:
                return
            val = board[r][c]
            seen.add((r,c))
            tmp = cur
            cur = cur.children[val]
            cur_str += val
            if cur.is_word and cur_str not in res:
                res.add(cur_str)
            dirs = [
                    [r+1,c],
                    [r-1,c],
                    [r,c+1],
                    [r,c-1],
            ]

            for dir in dirs:
                dfs(dir[0], dir[1], cur, cur_str)

            seen.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)

sol = Solution()


board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]

words = ["bat","cat","back","backend","stack"]

words = ["oa","oaa"]

print(sol.findWords(board,words))
