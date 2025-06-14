#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "node.h"

void free_list(Node *node) {
  if (node == NULL) {
    return;
  }
  Node * next = node->next;
  free(node);
  free_list(next);
}

bool contains_cycle(Node * head) {
  if (head == NULL) {
    return false;
  }

  Node *slow = head;
  Node *fast = head->next;

  while (fast != NULL && fast->next != NULL) {
    if (slow == fast) {
      return true;
    }

    slow = slow->next;
    fast = fast->next->next;
  }
  return false;
}
