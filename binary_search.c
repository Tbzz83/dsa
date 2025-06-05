#include <stdio.h>
#include <stdlib.h>

void sort_arr(int arr[], int arr_len) {
  // Still broke
  // Need to do multiple passes
  int l, r;
  r = 1;
  l = 0;

  if (arr_len > 0) {
    for ( r; r < arr_len; r ++) {
      if (arr[r] < arr[l]) {
        int temp = arr[r];
        arr[r] = arr[l];
        arr[l] = temp;
      }
      l++;
    }
  }
}

void print_list(int arr[], int arr_len) {
  for (int i = 0; i < arr_len ; i++) {
    printf("%d", arr[i]);
  }
  printf("\n");
}

int search_arr(int arr[], int target, int arr_len) {
  // Array must be sorted

  int l, r;
  l = 0;
  r = arr_len - 1;

  while ( l <= r) {
    int m = (l + r) / 2;
    if (arr[m] == target) {
      return m;
    } else if (arr[m] > target) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return -1;
}

int main()
{
  int arr[] = {1,3,2,4,5,6};
  int arr_len = sizeof(arr)/sizeof(arr[0]);
  int target = 5;
  int idx = search_arr(arr, target, arr_len);

  if (idx != -1) {
    printf("index of target '%d' is '%d'\n", target, idx);
  }

  printf("before sorting\n");
  print_list(arr, arr_len);
  sort_arr(arr, arr_len);
  printf("after sorting\n");
  print_list(arr, arr_len);

  return 0;
}