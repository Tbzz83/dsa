package main

import (
  "fmt"
  "sort"
)

func combinationSum2(candidates []int, target int) [][]int {
  var res [][]int

  sort.Ints(candidates)

  var backtrack func(i, curSum int, subset[]int)

  backtrack = func(i, curSum int, subset []int) {
    if curSum == target {
      tmp := make([]int, len(subset))
      copy(tmp, subset)
      res = append(res, tmp)
      return
    } else if i > len(candidates)-1 || curSum > target {
      return
    }

    subset = append(subset, candidates[i])
    backtrack(i+1, curSum+candidates[i], subset)
    subset = subset[:len(subset)-1]

    for i+1 < len(candidates) && candidates[i] == candidates[i+1] {
      i++
    }

    backtrack(i+1, curSum, subset)
  }

  backtrack(0, 0, []int{})

  return res
}

func main() {
  //candidates := []int{10,1,2,7,6,1,5}
  candidates := []int{2,5,2,1,2}
  targetInt := 5
  res := combinationSum2(candidates, targetInt)
  fmt.Println(res)
}
