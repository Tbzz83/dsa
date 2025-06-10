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

int nodes_in_tree(Node * node) {
  // Returns the number of nodes in the tree
  if (node == NULL) {
    return 0;
  }

  return 1 + nodes_in_tree(node->left) + nodes_in_tree(node->right);

}

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

  return 0;
}
