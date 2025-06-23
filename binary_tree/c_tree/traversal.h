#include "node.h"
#include <stdlib.h>
int * inorder_dfs(Node *node, int * inorder_arr) {
  if (node->left)
  {
    inorder_arr = inorder_dfs(node->left, inorder_arr);
  }

  *inorder_arr = node->data;
  inorder_arr++;

  if (node->right)
  {
    inorder_arr = inorder_dfs(node->right, inorder_arr);
  }

  return inorder_arr;
}

int * inorder_traversal(Node * node, size_t node_count) {
  // Return inorder array from the tree
  int *inorder_arr = (int*) malloc(sizeof(int)*node_count);
  int *head = inorder_arr;
  inorder_dfs(node, inorder_arr);
  return head;
}

int * preorder_dfs(Node *node, int * preorder_arr) {
  *preorder_arr = node->data;
  preorder_arr++;

  if (node->left != NULL)
  {
    preorder_arr = preorder_dfs(node->left, preorder_arr);
  }
  
  if (node->right != NULL)
  {
    preorder_arr = preorder_dfs(node->right, preorder_arr);
  }

  return preorder_arr;
}


int * preorder_traversal(Node * node, size_t node_count) {
  // return preorder array from the tree
  int *preorder_arr = (int*) malloc(sizeof(int)*node_count);
  int *head = preorder_arr;
  preorder_dfs(node, preorder_arr);
  return head;
}

int * postorder_dfs(Node *node, int * postorder_arr) {

  if (node->left != NULL)
  {
    postorder_arr = postorder_dfs(node->left, postorder_arr);
  }
  
  if (node->right != NULL)
  {
    postorder_arr = postorder_dfs(node->right, postorder_arr);
  }

  *postorder_arr = node->data;
  postorder_arr++;

  return postorder_arr;
}

int * postorder_traversal(Node * node, size_t node_count) {
  int *postorder_arr = (int*) malloc(sizeof(int)*node_count);
  int *head = postorder_arr;
  postorder_dfs(node, postorder_arr);
  return head;
}

