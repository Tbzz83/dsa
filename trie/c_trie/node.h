#ifndef TRIE_NODE 
#define TRIE_NODE 
#include <stdbool.h>
#include <stdlib.h>


typedef struct Node 
{
  struct Node **children; // arr
  bool end_of_word;
  char c;
} Node;

Node *create_node() {
  Node *node = (Node*) malloc(sizeof(Node)); // Alloc memory for itself
  Node **children = (Node**) malloc(26*sizeof(Node*)); // Alloc memory for at most 26 children
  node->children = children;
  return node;
}

#endif
