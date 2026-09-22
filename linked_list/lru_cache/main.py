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

    def ll_empty(self) -> bool:
        if not self.head and not self.tail:
#            if len(self.cache) != 0:
#                raise Exception(f"ll is empty while self.cache is non-empty: {self.cache}")

            return True
        if self.head and self.tail:
#            if len(self.cache) == 0:
#                raise Exception(f"ll is non-empty ({self.__repr__()}) while self.cache is empty: {self.cache}")
            return False

        raise Exception(f"self.head is {self.head} while self.tail is {self.tail}")

    def at_capacity(self):
        return self.num_nodes == self.capacity

    def get(self, key: int) -> int:
        if self.ll_empty():
            return -1

        elif key in self.cache:
            node = self._delete_node(self.cache[key])
            value = node.value
            self._insert_node(node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Create new node based on key, value.
        if at capacity, calls remove_lru()
        inserts new node.
        Handles accounting of metadata
        """

        # If our key exists, simply delete it first
        # It is simpler to do it this way than
        # overwriting the value of an existing node
        if key in self.cache:
            node = self._delete_node(self.cache[key])
            del self.cache[key]
            del node
            self.num_nodes -= 1
            
        new_node = Node(key,value)

        if self.at_capacity():
            self.remove_lru()

        self._insert_node(new_node)
        self.cache[key] = new_node
        self.num_nodes += 1

    def _insert_node(self, node: Node) -> None:
        """
        Inserts given node into the ll
        This method does not perform any accounting of metadata.
        """
        if self.ll_empty():
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None


        # Can safely assume our ll is non-empty
        else:
            # Update new node
            node.prev = self.tail
            node.next = None

            # Update tail
            self.tail.next = node
            self.tail = node

    def remove_lru(self):
        """
        Gets the lru node and calls _delete_node(lru_node)
        Handles accounting of metadata
        """
        if self.ll_empty():
            return

        lru_node = self.head
        lru_key = lru_node.key

        _ = self._delete_node(lru_node)
        self.num_nodes -= 1
        del self.cache[lru_key]

    def _delete_node(self, node: Node) -> Node:
        """
        Removes given node from the ll.
        This method may update self.head and self.tail.
        This method does not perform any accounting of metadata.
        """

        # In between two nodes
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            return node

        # Node is at start of ll
        if not node.prev and node.next:
            node.next.prev = node.prev
            self.head = node.next
            return node

        # Node is at end of ll
        if node.prev and not node.next:
            node.prev.next = node.next
            self.tail = node.prev
            return node

        # We are the only node in the ll, and the capacity must be 1
        self.head = self.tail = None
        return node

i = 0
cache = None
res = []
input = ["LRUCache", [5], "get", [80], "put", [1,100], "get", [1], "put", [2,139], "get", [2], "get", [1]]
#input = ["LRUCache", [5], "get", [80], "put", [1,100], "get", [1], "put", [2,139], "get", [2]]
#input = ["LRUCache", [5], "get", [80], "put", [1,100], "get", [1] ]
input = ["LRUCache", [2], "get", [2], "put", [2, 6], "get", [1], "put", [1, 5], "put", [1, 2], "get", [1], "get", [2]]
while i < len(input):
    command, args = input[i], input[i+1]

    if command == "LRUCache":
        cache = LRUCache(args[0])
        res.append(None)

    elif command == "put":
        k,v = args[0], args[1]
        cache.put(k,v)
        res.append(None)

    elif command == "get":
        k = args[0]
        res.append(cache.get(k))

    else:
        raise Exception(f"Unknown command {command}")

    i += 2

print(res)
print(cache)
