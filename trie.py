class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        # children['a'] = Node

class PrefixTree:
    def __init__(self):
      self.root = Node()

    def insert(self, word: str) -> None:
      cur = self.root
      for c in word:
        if c not in cur.children:
          cur.children[c] = Node()
        cur = cur.children[c]
      cur.end_of_word = True

    def search(self, word: str) -> bool:
      cur = self.root
      for c in word:
        if c not in cur.children:
          return False
        cur = cur.children[c]
      return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:


         
