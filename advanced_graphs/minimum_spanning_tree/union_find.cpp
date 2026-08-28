/*
Task here is to implemenet
*/

#include <iostream>
#include <memory>

using namespace std;

// Using a global is a bit easier to demonstrate and 
// allows us to work with arrays and not vectors
const int SIZE = 5;

class UnionFind {
public: 
    shared_ptr<int> items[SIZE];

    UnionFind() {
        // Initialize items
        for (auto i = 0; i < SIZE; i++) {
            // Use unique_ptr
            items[i] = make_shared<int>(i);
        }
    }

    // Who is your parent
    int* find(int val) {
        if (*items[val] == val) {
            return items[val].get();
        }

        return find(*items[val]);
    }

    void unite(int a, int b) {
        auto a_rep = find(a);
        auto b_rep = find(b);
        items[b] = items[a];
    }
};

int main() {
    auto uf = UnionFind();
    uf.unite(1,2);
    uf.unite(3,4);
    uf.unite(2,3);
    // Should print '1'
    cout << *uf.find(4) << "\n";

//    cout << "---\n";
//
//    auto ptr_1 = uf.find(1);
//    cout << ptr_1 << "\n";
}
