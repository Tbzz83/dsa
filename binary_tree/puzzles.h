#include <stdbool.h>
#include <stdlib.h>
#include "node.h"

bool same_tree(Node * p, Node * q) {
  if (p == NULL && q == NULL) {
    return true;
  }

  if (p->data != q->data) {
    return false;
  }

  return same_tree(p->left, q->left) && same_tree(p->right, q->right);
}

bool subtree_of_other_tree(Node * root, Node * subroot) {
  if (subroot == NULL) {
    return true;
  } else if (root == NULL) {
    return false;
  }

  if (same_tree(root, subroot)) {
    return true;
  }

  return subtree_of_other_tree(root->left, subroot) || subtree_of_other_tree(root->right, subroot);
}

