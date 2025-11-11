package main

import "fmt"


// Memoization
func climbStairsMemoiz(n int) int {
 
  var dp func(cur int) int
  var memo = make(map[int]int)

  dp = func(cur int) int {
    if cur == n {
      return 1
    } else if cur > n {
      return 0
    }

    if _, ok := memo[cur]; !ok {
      memo[cur] = dp(cur+1) + dp(cur+2)
    } 

    return memo[cur]
  }

  dp(0)

  return memo[0]
}

// Tabulation
func climbStairsTabulation(n int) int {
  var t []int
  t = append(t, 1)
  t = append(t, 1)

  for i := 2; i <= n; i++ {
    t = append(t, t[i-1] + t[i-2])
  }


  fmt.Println(t)
  return t[len(t) -1]
}

// Bottom-up no cache
func climbStairs(n int) int {
  p1 := 1
  p2 := 1

  for i := 2; i <= n; i++ {
    tmp := p2
    p2 += p1
    p1 = tmp
  }

  return p2
}



func main() {
  search := 6

  fmt.Println("memoiz")
  res := climbStairsMemoiz(search)
  fmt.Println("res:", res)

  fmt.Println("tabulation")
  res = climbStairsTabulation(search)
  fmt.Println("res:", res)

  fmt.Println("no mem")
  res = climbStairs(search)
  fmt.Println("res:", res)
}
