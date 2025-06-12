#include <stdio.h>
#include "node.h"

bool char_in_children(Node **children, int child_decimal, char c) {
  Node **cur = children + child_decimal;
  // *cur is the pointer to the child Node
  if (*cur == NULL){
    printf("char: %c is NOT a child.\n", c);
    return false;
  } else {
    printf("char: %c is a child!\n", c);
    return true;
  }

  return false;
}

bool starts_with(Node *head, char *string, size_t string_len) {
  Node *cur = head;
  for (int i=0; i < string_len; i++) {
    int child_decimal = string[i]-'a';
    if (!char_in_children(cur->children, child_decimal, string[i])) {
      return false;
    }
    cur = *(cur->children + child_decimal); 
  }
  return true;
}

bool search(Node *head, char *string, size_t string_len) {
  // If node doesn't exist
  if (head == NULL) {
    return false;
  }

  Node *cur = head;

  for (int i=0; i < string_len; i++) {
    int child_decimal = string[i]-'a';
    
    if (string[i] == '.') {
      // '.' is a wildcard character
      for (int j=0; j <= 26; j++) {
        if (cur->children + j) {
          // &string[i+1] is the remaining string needed to search
          // string_len value is updated by subtracting the difference of the indices 
          // for characters already searched
          if (search(*(cur->children + j), &string[i+1], string_len - (i+1))) {
            return true;
          }
        }
      }
      // This check is needed in the event that we check if cur has any children
      // if it does not, but clearly our string is not empty because we went into the 
      // for loop, then we must return false. In this event, there are too many '.' characters
      // at the end of the word
      return false;
    } else if (char_in_children(cur->children, child_decimal, string[i])) {
      cur = *(cur->children + child_decimal);
    } else {
      return false;
    }
  }

  if (cur->end_of_word) {
    return true;
  }
  return false;
}

void insert(Node *head, char *string, size_t string_len) {
  Node *cur = head;
  printf("\ninserting '%s'...\n", string);
  for (int i=0; i < string_len; i++) {
    // Taking the decimal value of 'char' - 'a' returns indexes in the size of an array of 26 characters
    int child_decimal = string[i]-'a'; 
    
    if (char_in_children(cur->children, child_decimal, string[i])) {// if character is child
      cur = *(cur->children + child_decimal);
    } else { // else create new node, add it as a child for cur, cur = (*(cur->children)) + child_decimal
      Node *new_node = create_node(); 
      *(cur->children + child_decimal) = new_node;
      new_node->c = string[i];
      cur = new_node;
    }
  }
  cur->end_of_word = true;
}

