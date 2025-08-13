package main

import (
  "fmt"
)

// My solution
//func generateParenthesis(n int) []string{ 
//  var res []string
//  var sub string
//  var ps = map[string]int{"(": n, ")": n}
//
//  var backtrack func()
//
//  backtrack = func() {
//    if ps["("] == 0 && ps[")"] == 0 {
//      res = append(res, sub)
//      return
//    }
//
//    if ps["("] > 0 {
//      sub += "("
//      ps["("] -= 1
//      backtrack()
//      sub = sub[:len(sub)-1] //pop
//      ps["("] += 1
//    }
//
//    if ps[")"] > 0 && ps["("] < ps[")"]{
//      sub += ")"
//      ps[")"] -= 1
//      backtrack()
//      sub = sub[:len(sub)-1] //pop
//      ps[")"] += 1
//    }
//  }
//
//  backtrack()
//
//  return res
//}

// Simpler solution without using map
func generateParenthesis(n int) []string{ 
  var res []string
  var backtrack func(op, cl int, sub string) 

  backtrack = func(op, cl int, sub string) {
    if op == n && cl == n {
      res = append(res, sub)
      return
    }

    if op < n {
      backtrack(op+1, cl, sub + "(")
    }
    
    // the 'cl < n' case could be ingored but 
    // I'll leave it in case I come back here
    if cl < n && op > cl {
      backtrack(op, cl+1, sub + ")")
    }
  }

  backtrack(0, 0, "")

  return res
}

func main() {
  res := generateParenthesis(3)
  for _, r := range(res) {
    fmt.Println(r)
  }
}




