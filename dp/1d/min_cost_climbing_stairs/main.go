package main

import ("fmt")

func minCostClimbingStairsBacktrack(cost []int) int {
  //var res int

  var backtrack func(i, curCost int) int

  backtrack = func(i, curCost int) int {
    if i > len(cost) - 1 {
      return curCost
    }

    return min(backtrack(i+1,curCost+cost[i]), backtrack(i+2, curCost+cost[i]))
  }

  return min(backtrack(0,0), backtrack(1, 0))
}

func minCostClimbingStairsMemoiz(cost []int) int {
  var memo = make(map[int]int)

  var dp func(i int) int 
  
  dp = func(i int) int {
    if i >= len(cost) {
      return 0
    }

    _, ok := memo[i]
    if !ok {
      memo[i] = cost[i] + min(dp(i+1), dp(i+2))
    }

    return memo[i]
  }


  res := min(dp(0), dp(1))

  fmt.Println(memo)

  return res

}


func main() {
  fmt.Println("backtrack")
  price := minCostClimbingStairsBacktrack([]int{10,15,20})
  price2 := minCostClimbingStairsBacktrack([]int{1,100,1,1,1,100,1,1,100,1})
  fmt.Println("price1", price)
  fmt.Println("price2", price2)

  fmt.Println()

  fmt.Println("memoiz")
  price = minCostClimbingStairsMemoiz([]int{10,15,20})
  price2 = minCostClimbingStairsMemoiz([]int{1,100,1,1,1,100,1,1,100,1})
  fmt.Println("price1", price)
  fmt.Println("price2", price2)

}
