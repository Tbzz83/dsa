#include <iostream>
#include <stdexcept>
#include <memory>
#include <string>

using namespace std;

enum NodeColor {
    RED,
    BLACK,
};

class Node {
public:
    // Yes this will one day become and enum
    NodeColor color;
    int val;
    Node *parent;
    Node *l_child;
    Node *r_child;

    Node(int val, NodeColor color = NodeColor::BLACK) {
        if (color != NodeColor::RED && color != NodeColor::BLACK) {
            throw runtime_error("Node color must be 'red' or 'black'");
        }
        this->val = val;
        this->color = color;

        parent = nullptr;
        l_child = nullptr;
        r_child = nullptr;
    }
};


class RBT {
public:
    Node *root;

    RBT(Node * root) {
        this->root = root;
    }

    void print_self() {
        print_tree_from_node(this->root);
    }

    void print_tree_from_node(Node * node) {
        if (!node) {
            return;
        }

        cout << node->val << "\n";
        print_tree_from_node(node->l_child);
        print_tree_from_node(node->r_child);
    }

//    // Specify a new int val to add to the tree, and a new 
//    // node will be created and inserted into the tree
//    void create_node_and_insert(Node * node) {
//        // We always try and add a new node that is red first
//        insert_node(node);
//    }

    // Traverse the tree starting from node, and find and return
    // the parent of a new node based on new_node_val. This method
    // does not perform and insertion, just returns a ptr to the parent
    // node
    Node* find_leaf_for_new_node(Node * node, int new_node_val) {
        if (!node->l_child && !node->r_child) {
            if (new_node_val == node->val) {
                throw invalid_argument("New node has invalid value. Value for new node already in use");
            }
            return node;
        }

        if (new_node_val > node->val) {
            if (node->r_child) {
                find_leaf_for_new_node(node->r_child, new_node_val);
            } else {
                return node;
            }

        } else if (new_node_val < node->val) {
            if (node->l_child) {
                find_leaf_for_new_node(node->l_child, new_node_val);
            } else {
                return node;
            }
        } 

        // Can't have duplicate values in RBT
        throw invalid_argument("New node has invalid value. Value for new node already in use");
    }

    void insert_node(Node * node) {
        // Find parent (p) for new node
        auto p = find_leaf_for_new_node(root, node->val);

        // Check nodes parent(p) color
        auto p_color = p->color;

        switch (p_color) {
            case NodeColor::RED:
                if (node->val > p->val) {
                } else if (node->val < p->val) {
                } else {
                    throw invalid_argument("New node has invalid value. Value for new node already in use");
                }

                break;

            case NodeColor::BLACK:
                if (node->val > p->val) {
                    p->r_child = node;
                } else if (node->val < p->val) {
                    p->l_child = node;
                } else {
                    throw invalid_argument("New node has invalid value. Value for new node already in use");
                }
                break;

            default:
                throw invalid_argument("Parent node color invalid value");
                break;
        }
    }
};

int main() {
    auto root = Node(0,NodeColor::BLACK);
    auto new_node = Node(1,NodeColor::RED);
    auto rbt = RBT(&root);
    rbt.insert_node(&new_node);
    rbt.print_self();
}
