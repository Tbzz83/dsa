package main

import "fmt"

func robBacktrack(nums []int) int {

  var backtrack func(i, curSum int, firstUsed bool) int


  backtrack = func(i, curSum int, firstUsed bool) int {
    if i >= len(nums) {
      return curSum
    }

    
    a := backtrack(i+1, curSum, firstUsed)


    bVal := curSum+nums[i]
    bBool := firstUsed

    if firstUsed && i == len(nums) - 1 {
      bVal = curSum
    }

    if i == 0 {
      bBool = true
    }

    b := backtrack(i+2, bVal, bBool)

    fmt.Println(a,b)
    return max(a,b)
  }

  res := backtrack(0, 0, false)
  return res
}

func robMemo(nums []int) int {
  if len(nums) == 1 {
    return nums[0]
  } else if len(nums) == 0 {
    return 0
  }
  var memo = make(map[int]int)
  var dp func(i int) int 

  dp = func(i int) int {
    if i >= len(nums) {
      return 0 // No more houses to rob
    }

    if val, ok := memo[i]; ok {
      return val
    }

    rob := nums[i] + dp(i+2)

    skip := dp(i+1)

    memo[i] = max(rob, skip)

    return memo[i]
  }

  a := dp(1)
  fmt.Println(nums)
  nums = nums[:len(nums)-1]
  memo = make(map[int]int)
  b := dp(0)

  return max(a, b)
}


func main() {

  res := robBacktrack([]int{1,2,3,1})
  fmt.Println(res)

  fmt.Println()

  res = robMemo([]int{2,1,1,2})
  fmt.Println(res)
}
