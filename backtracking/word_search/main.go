package main

// https://leetcode.com/problems/word-search/description/

import (
  "fmt"
  "strconv"
)

func exist(board [][]byte, word string) bool {

  var backtrack func(i, r, c int) bool 
  var seen = make(map[string]bool)

  backtrack = func(i, r, c int) bool {
    key := strconv.Itoa(r) + strconv.Itoa(c) 
    used := seen[key]

    if i > len(word) - 1 {
      return true
    } else if r < 0 || 
              r > len(board)-1 || 
              c < 0 || 
              c > len(board[r])-1 ||
              word[i] != board[r][c] ||
              used {
      return false
    }

    seen[key] = true
    res := backtrack(i+1, r+1, c) || 
           backtrack(i+1, r, c+1) ||
           backtrack(i+1, r-1, c) ||
           backtrack(i+1, r, c-1) 
    seen[key] = false
    return res
  }

  for r := range(board) {
    for c := range(board[r]) {
      if backtrack(0, r, c) {
        return true
      }
    }
  }

  return false

}




func printBoard(board [][]byte) {
  for _, row := range(board) {
    for _, b := range(row) {
      fmt.Print(string(b))
    }
    fmt.Println()
  }
}
func main() {
  board := [][]byte {
    //{'a','a','b','a','a','b'},{'a','a','b','b','b','a'},{'a','a','a','a','b','a'},{'b','a','b','b','a','b'},{'a','b','b','a','b','a'},{'b','a','a','a','a','b'},
    {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'},

//  board := [][]byte {
//    {'A','B'},
//    {'C', 'D'},
  }
  printBoard(board)

  fmt.Println()

  //fmt.Println(exist(board, "bbbaabbbbbab"))
  fmt.Println(exist(board, "ABCCED"))
  //fmt.Println(exist(board, "aba"))
}
