#include <stdio.h>
#include <string.h>
#include "node.h"
#include "ll_fns.h"

void print_list(Node *head) {
  Node *temp = head;
  while (temp != NULL) {
    printf("%d", temp->val);
    if (temp->next != NULL) {
      printf("-");
    }
    temp = temp -> next;
  }
  printf("\n");
}


Node *build_ll(int vals[], int vals_len) {
  Node *pHead = create_node(vals[0]);
  Node *cur = pHead;
  for (int i = 1; i < vals_len ; i++ ) {
    Node *new_node = create_node(vals[i]);
    cur->next = new_node;
    cur = new_node;
  }
  return pHead;
} 

void remove_from_idx_n(Node **head, int idx) {
  Node *cur = *head;
  int i = 0;
  while (cur != NULL) {
    if (i == idx - 1) {
      // Set cur pointer to cur->next->next
      cur->next = cur->next->next;
    }
    cur = cur->next;
    i++;
  }
}

int main()
{  
  int vals[] = {1,2,3,4,5,6};
  int vals_len = sizeof(vals)/sizeof(vals[0]);
  Node *head = build_ll(vals, vals_len);
  print_list(head);
  remove_from_idx_n(&head, 4);
  print_list(head);
  free(head);
  
  // ==== Let's create a ll with a cycle ====
  Node *node_one = create_node(1);
  Node *node_two = create_node(2);
  Node *node_three = create_node(3);

  node_one->next = node_two;
  node_two->next = node_three;
  node_three->next = node_one;
  // print_list(node_one); // This would run endlessley 
  if (contains_cycle(node_one)) {
    printf("Linked list contains cycle.\n");
  } else {
    printf("Linked list doesn't contain cycle :).\n");
  }

  return 0;
}

