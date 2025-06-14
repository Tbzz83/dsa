#ifndef NODE
#define NODE
#include <stdlib.h>

typedef struct Node {
  int val;
  struct Node *next;
} Node;

Node *create_node(int val) {
  Node *pNode = (Node*) malloc(sizeof(Node));
  pNode->val = val;
  pNode->next = NULL;
  return pNode;
}
#endif
