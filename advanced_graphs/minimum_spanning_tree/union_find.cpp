/*
Task here is to implemenet
*/

#include <iostream>
#include <memory>

using namespace std;

// Using a global is a bit easier to demonstrate and 
// allows us to work with arrays and not vectors
const int SIZE = 5;

class UnionFindNode {
public:
    int val;
    shared_ptr<UnionFindNode> parent;

    UnionFindNode(int val) {
        this->val = val;
        parent = nullptr;
    }
};

class UnionFind {
public: 
    shared_ptr<UnionFindNode> items[SIZE];

    UnionFind() {
        // Initialize items
        for (auto i = 0; i < SIZE; i++) {
            // Use unique_ptr
            items[i] = make_shared<UnionFindNode>(UnionFindNode(i));
        }
    }

    // Return index of parent
    shared_ptr<UnionFindNode> find(int idx) {
        auto node = items[idx];
        auto p = node->parent;

        while (p) {
            auto tmp = p;
            p = p->parent;
            node = tmp;
        }

        return node;
    }

    void unite(int a, int b) {
        auto a_rep = find(a);
        auto b_rep = find(b);
        b_rep->parent = a_rep;
    }
};

int main() {
    auto uf = UnionFind();

    for (auto i = 0; i < SIZE; i++) {
        cout << uf.items[i] << "\n";
    }
    auto a = uf.find(0);
    auto b = uf.find(1);
    uf.unite(1,2);
    uf.unite(3,4);
    uf.unite(2,3);
    // Should print '1'
    cout << uf.find(4)->val << "\n";

//    cout << "---\n";
//
//    auto ptr_1 = uf.find(1);
//    cout << ptr_1 << "\n";
}
