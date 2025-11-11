package main

import (
	"fmt"
	"strconv"
)

/*
Given an integer array nums, find the subarray

with the largest sum, and return its sum.

NOTE

- a subarrary is a contiguous slice of the input array. Does not need to start from 0.

- a subarray can be of length 1.

- a subarray can be the entire input array

- just return the sum, not the subarray itself. 

- start from 0, iterate through array, calculate curSum.

- if curSum < 0 && nums[i] > 0, curSum should be reset. Because, curSum + nums[i] will never be
  greater than nums[i] alone. We use < for simplicity, because if curSum == 0, it resetting it doesn't matter 
  if it is reset.

- if curSum >= 0, curSum += nums[i].  i++.
*/

func simple(nums []int) int {
  if len(nums) < 1 {
    return 0
  }

  curSum := nums[0]
  res := curSum

  fmt.Println(nums[1:])
  for _, val := range nums[1:] {
    fmt.Println(val, curSum)
    if curSum < 0 { 
      curSum = val
    } else {
      curSum += val
    }
    res = max(res, curSum)
  }

  return res
}

func dp(nums []int) int {
  var cache map[string]int = make(map[string]int)
  var res int
  var dp func(l,r,sum int) 

  dp = func(l,r,sum int) {
    if l == r && r == len(nums) - 1 {
      cache[strconv.Itoa(l)+strconv.Itoa(r)] = nums[r]
      res = max(res, sum)
      return 
    }


    key := strconv.Itoa(l)+strconv.Itoa(r)
    res = max(res, sum)

    if _, ok := cache[key]; ok { 
      return 
    } else {
      cache[key] = sum
    }

    fmt.Println(nums[l:r+1], "sum:", sum)

    if r < len(nums) -1 {
      dp(l,r+1,sum+nums[r+1])
    }
    if l < r {
      dp(l+1,r,sum-nums[l])
    }
  }

  res = nums[0]
  dp(0,0,nums[0])

  return res
}


func maxSubArray(nums []int) int {
  var res int

  var backtrack func(l,r,sum int)

  backtrack = func(l,r,sum int) {
    if l == r && r == len(nums) - 1 {
      res = max(sum, res)
      return
    }

    fmt.Println(nums[l:r+1], "sum:", sum)
    res = max(sum, res)

    if r < len(nums) -1 {
      backtrack(l,r+1,sum+nums[r+1])
    }

    if l < r {
      backtrack(l+1,r,sum-nums[l])
    }
  }

  res = nums[0]
  backtrack(0,0,nums[0])
    

  return res
}



func main() {

  //fmt.Println(simple([]int{-2,1,-3,4,-1,2,1,-5,4}))
  fmt.Println(simple([]int{5,4,-1,7,8}))
  //fmt.Println(dp([]int{-2,1,-3,4}))
  //fmt.Println(maxSubArray([]int{-2,1,-3}))

}
