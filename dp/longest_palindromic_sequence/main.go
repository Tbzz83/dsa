package main

import "fmt"

/*
- palindrome reads same forward and backward

- aim for better than On


*/
func dp(s string) int {


}

func longestPalindromeSubseqBT(s string) int {
  var backtrack func(l int) int 

  backtrack = func(l int) int {
    if l >= len(s) {
      return 0
    }

    biggest := 0 

    for r := l; r <= len(s); r++ {
      if isPalindrome(s[l:r]) {
        biggest = max(biggest, r - l + 1)
      }

      biggest = max(biggest, backtrack(r+1))
    }

    return biggest
  }
    

  return backtrack(0)
}

func isPalindrome(s string) bool {
  l, r := 0, len(s) - 1

  for l < r {
    if s[l] != s[r] {return false}
    l++
    r--
  }

  return true
}

func main() {
  //res := longestPalindromeSubseqBT("cbbd")
  res := dp("cbbd")
  fmt.Println(res)
}
