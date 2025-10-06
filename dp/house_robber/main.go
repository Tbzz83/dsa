package main

import "fmt"

func Backtrack(nums []int) int {
  res := 0
  var backtrack func(i, sum, lastRobbed int)

  backtrack = func(i, sum, lastRobbed int) {
    if i >= len(nums) {
      res = max(res, sum)
      return
    }

    // Rob
    if i >= lastRobbed + 2 {
      backtrack(i+1, sum + nums[i], i)
    } 

    backtrack(i+1, sum, lastRobbed)
  }

  backtrack(0,0, -2)

  return res
}

func memoiz(nums []int) int {
  var cache = make(map[int]int)

  var dp func(i int) int

  dp = func(i int) int {
    if i >= len(nums) {
      return 0
    } else if i == len(nums) - 1 {
      return nums[i]
    }

    _, ok := cache[i]

    if !ok {
      cache[i] = max(nums[i] + dp(i + 2), dp(i+1))
    }

    return cache[i]
  }

  dp(0)

  return cache[0]

}

func main() {
  fmt.Println("House robber")
//  fmt.Println(Backtrack([]int{1,2,3,1}))
//  fmt.Println(Backtrack([]int{2,7,9,3,1}))
  fmt.Println(memoiz([]int{1,2,3,1}))
  fmt.Println(memoiz([]int{2,7,9,3,1}))
}
