package main

import "fmt"

/*
Top-Down memoization
the trick here is to use a 2d array to cache whether for the current index i 
if it is possible to find a solution to find target

memo = 
[
	[0,0,0]
	[0,0,0]
	[0,0,0]
]

setting a value to 2 means for memo[i][target] there is NO solution

*/


func printGrid(nums [][]int) {
	fmt.Println("---")
	for r := range(nums) {
		fmt.Println(nums[r])
	}

	fmt.Println("---")


}

func canPartition(nums []int) bool {
	var totSum = 0
	for _, num := range(nums) {
		totSum += num
	}

	if totSum % 2 != 0 {
		return false
	}

	target := totSum / 2

	var memo = make([][]int, len(nums)+1)
	for i := range(memo) {
		// '0' means not-initialized. 1 means possible, 2 means no solution
		memo[i] = make([]int, target+1)
	}

	var dp func(i int, target int) int 

	dp = func(i int, target int) int {
		printGrid(memo)
		if target == 0 {
			memo[i][target] = 1
			return 1 
		} else if i >= len(nums) || target < 0 {
			// No solution
			return 2
		}

		if memo[i][target] == 0 {
			if dp(i+1, target-nums[i]) == 1 || dp(i+1, target) == 1{
				memo[i][target] = 1
			} else {
				memo[i][target] = 2
			}
		}

		return memo[i][target]
	}

	return dp(0, target) == 1
}


func main() {
	nums := []int{2,3,1,4,2,2,10,100}
	fmt.Println(canPartition(nums))
}
