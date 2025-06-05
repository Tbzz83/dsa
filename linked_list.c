#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
  int val;
  struct Node *next;
} Node;

void printlist(Node *head) {
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

Node *createnode(int val) {
  Node *pNode = (Node*) malloc(sizeof(Node));
  pNode->val = val;
  pNode->next = NULL;
  return pNode;
}

Node *build_ll(int vals[], int vals_len) {
  Node *pHead = createnode(vals[0]);
  Node *cur = pHead;
  for (int i = 1; i < vals_len ; i++ ) {
    Node *new_node = createnode(vals[i]);
    cur->next = new_node;
    cur = new_node;
  }
  return pHead;
} 

void remove_from_idx_n(Node **head, int idx) {
  Node *cur = *head;
  printf("%d\n", cur->val);
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
  printlist(head);
  //remove_from_idx_n(&head, 4);
  printlist(head);

  return 0;
}