"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

    LRUCache(int capacity) Initialize the LRU cache of size capacity.
    int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1)O(1) average time complexity.

Solution:

Okay so basically whenever we call get, we need to say that this item was the most recently used.
So we want to know the prev and next used nodes as well. When we call get we will remove it from its
place, put it at the very end of the ll, connect prev->next. When we are at capacity and call put, we will
remove the node at the front of the ll, and put the new value at the end (most recently used)
"""

class Node:
    def __init__(self, key, value) -> None:
        self.prev: Node|None = None
        self.next: Node|None = None
        self.value: int = value
        self.key: int = key

    def __repr__(self) -> str:
        return f"({str(self.key)},{str(self.value)})"

class LRUCache:
    def __init__(self, capacity: int):
        self.num_nodes: int = 0
        self.capacity: int = capacity
        self.head: Node|None = None
        self.tail: Node|None = None
        self.cache: dict[int,Node] = {}

    def __repr__(self):
        cur = self.head
        res = ""

        while cur:
            res += f"{cur.__repr__()} -> "
            cur = cur.next

        return res


    def get(self, key: int) -> int:
        if key in self.cache:
            cur = self.cache[key]
            self.move_node_to_mru(cur)
            return cur.value
        else:
            return -1
        

    # Moves a node to most recently used
    def move_node_to_mru(self, node: Node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        elif node.next:
            self.head = node.next
            self.head.prev = None

        if self.tail:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        node.next = None

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur = self.cache[key]

            if cur.value != value:
                self.move_node_to_mru(cur)
                cur.value = value

            return

        new_node = Node(key,value)
        self.cache[key] = new_node
        self.num_nodes += 1

        if self.num_nodes == self.capacity + 1:
            self.remove_lru()

        if not self.tail:
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        if not self.head:
            self.head = new_node


    def remove_lru(self):
        if not self.head:
            return

        head = self.head
        self.head = self.head.next

        if self.head:
            self.head.prev = None

        del self.cache[head.key]
        self.num_nodes -= 1
        del head

cache = LRUCache(5)
cache.put(1,10)
cache.put(2,20)
cache.put(3,30)
cache.put(4,40)
cache.put(5,50)
cache.put(2,200)
cache.put(4,40)
print(cache.get(2))
print(cache)
#print(cache.head, cache.head.prev, cache.head.next)
#print(cache.tail, cache.tail.prev, cache.tail.next)
#cache.get(2)
#
#print(cache)
#cache.get(2)
#print(cache.cache)
#print(cache.get(1))
#print(cache.get(2))
#cache.put(3,30)
#cache.get(2)
#cache.get(1)
