package main
import (
  "fmt"
)


func plusMinus(nums []int, target int) int {
  var backtrack func(idx, curSum int) 
  var res int

  backtrack = func(idx, curSum int) {

    for i := idx; i < len(nums); i++ {
      nums[i] *= -1
      backtrack(i+1, curSum + nums[i])
      nums[i] *= -1
      curSum += nums[i]
    }

    if curSum == target {
      res ++
    }
  }

  backtrack(0, 0)

  return res
}

func main() {
  nums := []int{1,1,1,1,1}
  res := plusMinus(nums, 3)
  fmt.Println(res)
}
