#include <stdio.h>
#include <stdlib.h>


typedef struct Node 
{
  int data;
  struct Node *left;
  struct Node *right;
} Node;

Node * createnode(int val)
{
  Node * pNode = (Node*) malloc(sizeof(Node)); // Allocate memory on the heap
  pNode->data = val;
  pNode->left = NULL;
  pNode->right = NULL;
  return pNode;
}

void putnode(Node * node, Node * new_node) {
  if (new_node->data < node->data) {
    if (node->left == NULL) {
      node->left = new_node;
    } else { // Call putnode on left
      putnode(node->left, new_node);
    }
  } else if ( new_node->data > node->data) {
    if (node->right == NULL) {
      node->right = new_node;
    } else { // Call putnode on right
      putnode(node->right, new_node);
    }
  } else { // Invalid node, violates binary tree
    printf("Invalid value for new node: %d as current node value is: %d\n", new_node->data, node->data);
    exit(1);
  }
}

Node * buildtree(int vals[], int vals_len) 
{
  Node * root = createnode(vals[0]);
  for (int i = 1; i < vals_len; i++)
  {
    Node * new_node = createnode(vals[i]);
    printf("creating new node with value: %d\n", new_node->data);
    putnode(root, new_node);
  }
  return root;
}

void checktree(Node * node) {
  if (node == NULL) {
    return;
  }
  printf("%d\n", node->data);
  checktree(node->left);
  checktree(node->right);
  return;
}

void freetree(Node *node) {
  if (node == NULL) return;
  freetree(node->left);
  freetree(node->right);
  free(node);
}

int main()
{
  int vals[] = {5,3,1,4,8,7,9};
  Node * head = buildtree(vals, sizeof(vals)/sizeof(vals[0]));
  checktree(head);
  freetree(head);
//  Node * pNode1 = createnode(5);
//  printf("node value: %d\n", pNode1->data);
//  free(pNode1);
//
//  Node * pNode2 = createnode(6);
//  pNode1->right = pNode1;
//  printf("node1.right.val: %d\n", pNode1->right->data);
//
//  free(pNode2);

  return 0;
}