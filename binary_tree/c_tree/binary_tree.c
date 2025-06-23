#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "traversal.h"
#include "node.h"
#include "puzzles.h"

// TODO
// Figure out how to print the tree
// subtree of binary tree function

Node * create_node(int val)
{
  Node * pNode = (Node*) malloc(sizeof(Node)); // Allocate memory on the heap
  pNode->data = val;
  pNode->left = NULL;
  pNode->right = NULL;
  return pNode;
}

void print_int_arr(int * arr, size_t size) {
  printf("[");
  for (int i = 0; i < size;i++)
  {
    printf("%d", arr[i]);
    if (i != size -1)
    {
      printf(",");
    }
  }
  printf("]");
  printf("\n");
}

void add_node(Node * node, Node * new_node) {
  if (new_node->data < node->data) {
    if (node->left == NULL) {
      node->left = new_node;
    } else { // Call add_node on left
      add_node(node->left, new_node);
    }
  } else if ( new_node->data > node->data) {
    if (node->right == NULL) {
      node->right = new_node;
    } else { // Call add_node on right
      add_node(node->right, new_node);
    }
  } else { // Invalid node, violates binary tree
    printf("Invalid value for new node: %d as current node value is: %d\n", new_node->data, node->data);
    exit(1);
  }
}


Node * build_tree_from_preorder(int vals[], int vals_len) {
  // Builds binary tree based a valid tree from an preorder traversal based array
  printf("\n");
  printf("creating root node with value: %d\n", vals[0]);
  Node * root = create_node(vals[0]);
  for (int i = 1; i < vals_len; i++)
  {
    printf("creating new node with value: %d\n", vals[i]);
    Node * new_node = create_node(vals[i]);
    add_node(root, new_node);
  }
  return root;
}

int nodes_in_tree(Node * node) {
  // Returns the number of nodes in the tree
  if (node == NULL) {
    return 0;
  }

  return 1 + nodes_in_tree(node->left) + nodes_in_tree(node->right);

}


void print_tree(Node * node, int tree_height) {
  // TODO 
  // Create queue data structure
  return;
}

int get_tree_height(Node *node) {
  if (node == NULL) {
    return 0;
  }

  int left_height = get_tree_height(node->left);
  int right_height = get_tree_height(node->right);

  if (right_height >= left_height) {
    return 1 + right_height;
  } else {
    return 1 + left_height;
  }
}

void free_tree(Node *node) {
  if (node == NULL) return;
  free_tree(node->left);
  free_tree(node->right);
  free(node);
}


int main()
{
  //int vals[] = {14,9,1,5,10,18,17,22,21,24};
  int vals[] = {7,1,3,2,4};
  Node * head = build_tree_from_preorder(vals, sizeof(vals)/sizeof(vals[0]));
  if (head == NULL)
  {
    printf("Error. node was not created successfully\n");
    return 1;
  }
  
  int node_count = nodes_in_tree(head);

  printf("\n");
  printf("Number of nodes in tree is: %d\n", node_count);

  int *inorder_arr = inorder_traversal(head, node_count);
  printf("\n");
  printf("inorder traversal array:\n");
  print_int_arr(inorder_arr, node_count);
  free(inorder_arr);

  int *preorder_arr = preorder_traversal(head, node_count);
  printf("\n");
  printf("preorder traversal array:\n");
  print_int_arr(preorder_arr, node_count);
  free(preorder_arr);

  int *postorder_arr = postorder_traversal(head, node_count);
  printf("\n");
  printf("postorder traversal array:\n");
  print_int_arr(postorder_arr, node_count);
  free(postorder_arr);
  
  int height = get_tree_height(head);
  print_tree(head, height);
  printf("\n");
  printf("Tree height: %d\n", height);
  free_tree(head);
  
  //contains_subtree
  printf("\n");
  int root_preorder[] = {4,2,1,3,5};
  int subroot_preorder[] = {2,1,3};
  Node * root = build_tree_from_preorder(root_preorder, sizeof(root_preorder)/sizeof(root_preorder[0]));
  Node * subroot = build_tree_from_preorder(subroot_preorder, sizeof(subroot_preorder)/sizeof(subroot_preorder[0]));
  printf("\n");
  bool subtree = subtree_of_other_tree(root, subroot);
  if (subtree) {
    printf("subroot is a subtree of root!\n");
  } else {
    printf("subroot is 'not' a subtree of root\n");
  }
  printf("\n");


  return 0;
}




