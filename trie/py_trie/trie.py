class Node:
    children: dict[str, 'Node']
    end_of_word: bool

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        # children['a'] = Node


class PrefixTree:
    root: Node

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            c = c.lower()
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

    def startsWith(self, prefix: str):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


def main():
    prefix_tree = PrefixTree()
    prefix_tree.insert("apple")
    prefix_tree.insert("ape")
    prefix_tree.insert("apply")

    # Return True
    print(f"Searching for 'apple': {prefix_tree.search("apple")}")
    # Also return True
    print(f"starts with 'ape'? {prefix_tree.startsWith("ape")}")


main()
