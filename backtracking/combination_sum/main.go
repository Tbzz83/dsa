package main

import "fmt"

func combinationSum(candidates []int, target int) [][]int {
  var res [][]int

  var backtrack func(idx, curSum int, subset []int)

  backtrack = func(idx, curSum int, subset []int) {
    if curSum == target {
      tmp := make([]int, len(subset))
      copy(tmp, subset)
      res = append(res, tmp)
      return
    } else if curSum > target || idx > len(candidates) - 1 { 
      return
    } 

    backtrack(idx, curSum + candidates[idx], append(subset, candidates[idx]))
    backtrack(idx+1, curSum, subset)
  }

  backtrack(0, 0, []int{})



  return res

}

func main() {
  res := combinationSum([]int{2,5,6,9}, 9)
  fmt.Println(res)
}
