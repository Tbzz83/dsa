package main

import (
  "fmt"
)

func subsetsWithDup(nums []int) *[][]int {
  res := new([][]int)
  startingSubset := []int{}
  startingIdx := 0

  backtrack(startingSubset, nums, startingIdx, res)

  return res
}

func backtrack(subset, nums []int, idx int, res *[][]int) {
  if idx > len(nums) -1 {
    tmp := make([]int, len(subset))
    copy(tmp, subset)
    *res = append(*res, tmp)
    return
  }

  subset = append(subset, nums[idx])
  backtrack(subset, nums, idx+1, res)
  subset = subset[:len(subset)-1]
  for idx+1 < len(nums) && nums[idx] == nums[idx+1] {
    idx++
  }

  backtrack(subset, nums, idx+1, res)

}


func main() {
  nums := []int{1,2,2}
  res := subsetsWithDup(nums)
  fmt.Println(res)
}
