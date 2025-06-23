#include <stdio.h>
#include <string.h>
#include "node.h"
#include "node_fns.h"

//TODO
//Command-line-interface

int main() {
  Node *head = create_node();

  // ONLY INSERT LOWERCASE WORDS FOR NOW
  char apple[] = "apple";
  char ape[] = "ape";
  char banana[] = "banana";
  char pear[] = "pear";

  insert(head, apple, strlen(apple));
  insert(head, ape, strlen(ape));
  insert(head, banana, strlen(banana));
  insert(head, pear, strlen(pear));
 
  printf("\n");
  char apples[] = "a..";
  // Let's search for apple and see if it returns 'true'
  if (search(head, apples, strlen(apples))) {
    printf("%s is found in search!\n", apples);
  } else {
    printf("%s is NOT found in search.\n", apples);
  }
  
  printf("\n");
  char starts_with_test[] = "pe";
  // Let's see what words start with contents of 'starts_with_test'
  if (starts_with(head, starts_with_test, strlen(starts_with_test))) {
    printf("words do start with '%s'!\n", starts_with_test);
  } else {
    printf("words DO NOT start with '%s'.\n", starts_with_test);
  }
  
  free(head);
  return 0;
}
