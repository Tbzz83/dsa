package main

import "fmt"

/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Could also jump 2 steps to index 2, then 1 step to index 3, then 1 step to last index

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

---
Example 1:
Input: nums = [2,3,1,1,4]

Start at index i = 0

maxJump = nums[i] = 2

question:
Am I at last index?

choice:
1. use maxJump to increment i by 2 -> nums[i+2] = 1 -> question: Am I at last index? ... RECURRENCE
2. use maxJump - 1 -> nums[i+1] = 3 -> question: Am I at last index? ... RECURRENCE
3. can't use maxJump -2: == 0, so would repeat

choices are from 1->nums[i] == 1->maxJump (inclusive)

*/

// Top down memoization
func canJump(nums []int) bool {
  var dp func(i int) bool
  var cache = make(map[int]bool)
  cache[len(nums)-1] = true // if at last index return true

  dp = func(i int) bool {
    if possible, ok := cache[i]; ok {
      return possible
    }

    maxJump := nums[i]
    possible := false

    for j := 1; j <= maxJump; j++ {
      if possible { break }
      possible = dp(j+i) 
    }

    cache[i] = possible

    return possible
  }

  possible := dp(0)

  fmt.Println(cache)
  return possible
}

func main() {
//  fmt.Println(canJump([]int{2,3,1,1,4}))
  fmt.Println(canJump([]int{3,3,1,0,4}))
}
