package main

import (
  "fmt"
)

func permute(nums []int) [][]int {
  var res [][]int
  var backtrack func()
  var perm []int
  var count = make(map[int]int)

  for _, num := range(nums) {
    _, ok := count[num]
    if !ok {
      count[num] = 1
    } else {
      count[num] += 1
    }
  }

  fmt.Println(perm, count)
  
  backtrack = func() {
    if len(perm) == len(nums) {
      tmp := make([]int, len(perm))
      copy(tmp, perm)
      res = append(res, tmp)
      return
    }


    for n := range(count) {
      if count[n] > 0 {
        perm = append(perm, n)
        count[n] -= 1

        backtrack()

        count[n] += 1
        perm = perm[:len(perm)-1]
      }
    }


  }

  backtrack() 
  return res
}

func main() {
  nums := []int{1,1,2}
  res := permute(nums)
  fmt.Println(res)
}
