#include <stdio.h>
#include <stdlib.h>

void sort_arr(int arr[], int arr_len) {
  int i, j;
  i = 1;

  if (arr_len == 0) {
    return;
  }

  for (i; i < arr_len; i++) {
    j = 0; // reset j
    for (j; j < arr_len - 1; j++) {
      if (arr[j] > arr[j+1]) {
        int tmp = arr[j+1];
        arr[j+1] = arr[j];
        arr[j] = tmp;
      }
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
  sort_arr(arr, arr_len);

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
  int arr[] = {2,8,5,3,9,4,1};
  int arr_len = sizeof(arr)/sizeof(arr[0]);
  int target = 5;
  int idx = search_arr(arr, target, arr_len);

  if (idx != -1) {
    printf("index of target '%d' is '%d'\n", target, idx);
  }
  print_list(arr, arr_len);

//  printf("before sorting\n");
//  print_list(arr, arr_len);
//  sort_arr(arr, arr_len);
//  printf("after sorting\n");
//  print_list(arr, arr_len);

  return 0;
}
