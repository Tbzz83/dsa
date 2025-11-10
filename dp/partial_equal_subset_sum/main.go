package main

import "fmt"

func canPartition(nums []int) bool {
	var totSum = 0
	var res = false
	for _, num := range(nums) {
		totSum += num
	}

	if totSum % 2 != 0 {
		return false
	}

	target := totSum / 2

	var memo = make([][]bool, len(nums)+1)
	for i := range(memo) {
		memo[i] = make([]bool, target+1)
		fmt.Println(memo[i])
	}

	var dp = func(i int, target int) bool {
		if target == 0 {
			memo[i][target] = true
			return true
		}

	}


	return res
}


func main() {
	nums := []int{1,2,3}
	fmt.Println(canPartition(nums))
}
