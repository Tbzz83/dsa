from typing import Optional

class Node:
    def __init__(self, val=0, neighbors: Optional[list["Node"]] = None) -> None:
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors else []
