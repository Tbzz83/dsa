package main

import (
	"fmt"
)

func partition(s string) [][]string {
  var res [][]string

  var backtrack func(subset []string, idx int) 

  backtrack = func(subset []string, idx int) {
    if idx > len(s) - 1 {
      tmp := make([]string, len(subset))
      copy(tmp, subset)
      res = append(res, tmp)
      return
    }

    for i := idx; i < len(s); i++ {
      if isPalindrome(string(s[idx:i+1])) {
        substr := string(s[idx:i+1])

        subset = append(subset, substr)
        backtrack(subset, i+1)
        subset = subset[:len(subset)-1]
      } 
    }
  }

  backtrack([]string{}, 0)

  return res
}

func isPalindrome(s string) bool {
  l, r := 0, len(s) - 1

  for l < r {
    if s[l] != s[r] {
      return false
    }

    l++
    r--
  }

  return true
}

func main() {
  partition("abaca")
}
