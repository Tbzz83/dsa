package main

import (
  "fmt"
)

func permute(nums []int) [][]int {
  var res [][]int
  var backtrack func(i int)

  backtrack = func(i int) {
    if i > len(nums) - 1 {
      tmp := make([]int, len(nums))
      copy(tmp, nums)
      res = append(res, tmp)
      return
    }

    for j := i; j < len(nums); j++ {
      fmt.Println("nums[i], nums[j]:", nums[i], nums[j])
      // swap values
      nums[i], nums[j] = nums[j], nums[i]

      backtrack(i+1)

      // unswap
      nums[i], nums[j] = nums[j], nums[i]
    } 
  }

  backtrack(0) 
  return res
}

func main() {
  nums := []int{1,2,3}
  res := permute(nums)
  fmt.Println(res)
}
