#include <stdio.h>
#include <stdlib.h>

// TODO
// Figure out how to print the tree

typedef struct Node 
{
  int data;
  struct Node *left;
  struct Node *right;
} Node;

Node * create_node(int val)
{
  Node * pNode = (Node*) malloc(sizeof(Node)); // Allocate memory on the heap
  pNode->data = val;
  pNode->left = NULL;
  pNode->right = NULL;
  return pNode;
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

Node * build_tree(int vals[], int vals_len) 
{
  Node * root = create_node(vals[0]);
  for (int i = 1; i < vals_len; i++)
  {
    Node * new_node = create_node(vals[i]);
    printf("creating new node with value: %d\n", new_node->data);
    add_node(root, new_node);
  }
  return root;
}

void print_tree(Node * node) {
  if (node == NULL) {
    return;
  }
  printf("%d\n", node->data);
  print_tree(node->left);
  print_tree(node->right);
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
  int vals[] = {14,9,1,5,10,18,17,22,21,24};
  Node * head = build_tree(vals, sizeof(vals)/sizeof(vals[0]));
  print_tree(head);
  int height = get_tree_height(head);
  printf("Tree height: %d\n", height);
  free_tree(head);

  return 0;
}