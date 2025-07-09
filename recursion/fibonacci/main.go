package main

import (
  "fmt"
)

// 0 , 1, 1, 2, 3, 5, 8, 13, 21, 34 etc... 
// given an integer 'n', find the nth number of the fibonacci sequence

func fib(n int) int {
  if n == 0 || n == 1 {
    return n
  } 

  fmt.Println("n", n)

  return fib(n-1) + fib(n-2)
}

// return (fib(2) -> (fib(1) = 1) + (fib(0) = 0) = 1) + (1)

func main() {
  n := fib(3)
  fmt.Println(n)
}
