
class UnionFind:
    """
    Credit: https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
    In English:
    Say you have 5 different items: 0,1,2,3,4
    You initialize a list in that range: list = [0,1,2,3,4]
    This initializes such that each item is the sole member of its own set

    If you unionize two items (say 1,2), what happens is you arbitrarily pick
    either index 1 or 2 and overwrite the item in the position with the other item:

    eg. [0,1,1,3,4]

    Now when you want to find the set that the item 2 belongs to, you look it up through 
    its index list[2] = 1. This means that item '2' is apart of the set where item '1' is the
    representative (owner)

    if list[i] = i it means that i is the rep (owner)

    thus you can see that eventually if you keep unionizing you will get 
    list = [1,1,1,1,1]. ie. all items [0-4] are apart of one set where item '1' is 
    the representative

    Basically you are using the list elements like a pointer, and the list index positions as identification
    of what item actually 'exists' there (because nothing exists there really except the pointer to another index position)

    pretty neat! You could implement this using an array in a lower level language, where the array stores literal pointers
    to the actual data. See union_find.cpp!
    """
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))
    
    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.unite(2,1)
    print(uf.find(2))
