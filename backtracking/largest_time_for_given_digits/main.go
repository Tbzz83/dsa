package main

import (
  "fmt"
)

func largestTimeFromDigits(arr []int) {
  var res [][]int
  var backtrack func(substr []int, search []int)

  backtrack = func(substr []int, search []int) {
    if len(substr) == len(arr) {
      tmp := make([]int, len(substr))
      copy(tmp, substr)
      res = append(res, tmp)
      return
    }

    for i, num := range(search) {
      newSearch := append([]int{}, search[:i]...)
      newSearch = append(newSearch, search[i+1:]...)

      //newSubstr := make([]int, len(substr))
      //copy(newSubstr, substr)
      //newSubstr = append(newSubstr, num)
      substr = append(substr, num)
      //backtrack(newSubstr, newSearch)
      backtrack(substr, newSearch)

    }
  }

  backtrack([]int{}, arr) 

  fmt.Println(res)
}


func main() {
  largestTimeFromDigits([]int{1,2,3,4})
}
