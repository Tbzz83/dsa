package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
  var stack []int

  for _, token := range(tokens) {
    switch token {
    case "+":
      last := len(stack) - 1
      a := stack[last]
      stack = stack[:last]

      last = len(stack) - 1
      b := stack[last]
      stack = stack[:last]

      stack = append(stack, a + b)
    case "*":
      last := len(stack) - 1
      a := stack[last]
      stack = stack[:last]

      last = len(stack) - 1
      b := stack[last]
      stack = stack[:last]

      stack = append(stack, a * b)
    case "-":
      last := len(stack) - 1
      a := stack[last]
      stack = stack[:last]

      last = len(stack) - 1
      b := stack[last]
      stack = stack[:last]

      stack = append(stack, b - a)
    case "/":
      last := len(stack) - 1
      a := stack[last]
      stack = stack[:last]

      last = len(stack) - 1
      b := stack[last]
      stack = stack[:last]

      stack = append(stack, b / a)
    default:
      // integer
      tokenInt, _ := strconv.Atoi(token)
      stack = append(stack, tokenInt)
    }
  }

  return stack[0]
}



func main() {
  
  fmt.Println(evalRPN([]string{"2", "1", "+", "3", "*"}))
  fmt.Println()
  fmt.Println(evalRPN([]string{"4","13","5","/","+"}))
  fmt.Println()
  fmt.Println(evalRPN([]string{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}))

}
