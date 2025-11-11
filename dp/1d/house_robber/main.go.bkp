package main

import "fmt"

func robBacktrack(nums []int) int {
  var res int
  var backtrack func(i, curSum int) 

  backtrack = func(i, curSum int) {
    if i > len(nums) - 1 {
      res = max(res, curSum)
      return
    }

    backtrack(i+2, curSum+nums[i])
    backtrack(i+1, curSum)
  }

  backtrack(0, 0)

  return res
}

func robMemo(nums []int) int {
  var memo = make(map[int]int)
  var dp func(i, curSum int) int
  
  dp = func(i, curSum int) int {
    if i > len(nums) - 1 {
      return curSum // No more to rob
    }

    val, ok := memo[i]
    if ok {return val}

    memo[i] = max(dp(i+2, curSum+nums[i]), dp(i+1, curSum))

    return memo[i]

  }

  dp(0, 0)

  fmt.Println(memo)
  return memo[0]
}

func robTab(nums []int) int {

  if len(nums) == 1 {
    return nums[0]
  }

  var t = make([]int,0, len(nums))
  t = append(t, nums[len(nums)-1]) // if at last element, max price you could rob is that value
  nums = nums[:len(nums)-1]
  t = append(t, max(t[0], nums[len(nums)-1])) 
  nums = nums[:len(nums)-1]
  a, b := 0, 1

  for i := len(nums)-1; i >= 0; i-- {
    t = append(t, max(t[b], nums[i]+t[a]))
    a++
    b++
  }

  fmt.Println(t)

  fmt.Println("---")
  return t[len(t)-1]

}

func rob(nums []int) int {
  if len(nums) == 0 {
    return 0
  }

  if len(nums) == 1 {
    return nums[0]
  } 

  if len(nums) == 2 {
    return max(nums[0], nums[1])
  }

  a, b := nums[0], nums[1]

  for i := 2; i < len(nums) ; i++ {
    a, b = max(a, b), max(a+nums[i], b)
  }

  return b

} 



func main() {
  res1 := robBacktrack([]int{1,2,3,1})
  fmt.Println(res1)

  fmt.Println()

  res2 := robBacktrack([]int{2,7,9,3,1})
  fmt.Println(res2)

  fmt.Println()
  res3 := robMemo([]int{1,2,3,1})
  fmt.Println(res3)

  fmt.Println()
  res4 := robTab([]int{2,7,9,3,1})
  fmt.Println(res4)

  fmt.Println()
  res5 := rob([]int{2,1,1,2})
  fmt.Println(res5)
}
