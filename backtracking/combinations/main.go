package main

import "fmt"

/*

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

NOTE

example: n = 4, k = 2

start from i==1:

choice: pick or skip i

pick i -> add to slice [i]

skip i -> leave slice alone []

increment i ++

choice: pick or skip i+1

pick i+1 -> add to slice [i,i+1]

skip i+1 -> leave slice alone [i]


Return values and base case:

Function should return a 2D array of all combinations.

if i > n: we should return our 2D array no matter what it is.

*/



/*
The below solution is inefficient, because of the merging of 2D slices
up the call stack. This tree of decisions cannot be optimized using DP, because
there are no overlapping sub-problems.
*/
func combineInefficient(n, k int) [][]int {

  var backtrack func(i int, res [][]int, sub []int) [][]int

  backtrack = func(i int, res [][]int, sub []int) [][]int {
    fmt.Println(sub)
    if len(sub) == k {
      var tmp []int = make([]int, len(sub))
      copy(tmp, sub)
      res = append(res, tmp)
      return res
    } else if i > n {
      return nil
    }


    pick := backtrack(i+1, res, append(sub, i))
    skip := backtrack(i+1, res, sub)

    res = append(res, pick...)
    res = append(res, skip...)

    return res
  }

  return backtrack(1, [][]int{}, []int{})
}

/*
Efficient solution. Typical backtracking approach
*/
func combine(n, k int) [][]int {
  res := [][]int{}

  var backtrack func(i int, sub []int)

  backtrack = func(i int, sub []int) {
    if len(sub) == k {
      tmp := make([]int, len(sub)) 
      copy(tmp, sub)
      res = append(res, tmp)
      return
    } else if i > n {
      return
    }

    // Pick
    backtrack(i+1, append(sub, i))
    // Skip
    backtrack(i+1, sub)
  }

  backtrack(1, []int{})

  return res
}


func main() {
  fmt.Println(combineInefficient(4,2))
  fmt.Println(combine(4,2))
}

