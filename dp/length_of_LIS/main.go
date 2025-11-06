package main

import "fmt"

// Memoization solution O(n^2) time: O(n) space
func lengthOfLIS(nums []int) int {
	var res int
	memo := make(map[int]int)
	var dp func(i int)int

	dp = func(i int)int {
		if i == len(nums) - 1 {
			memo[i] = 1
			return memo[i]
		} else if i >= len(nums) {
			return 0
		}

		if _, ok := memo[i]; ok {
			return memo[i]
		}

		memo[i] = 1

		for j := i+1; j < len(nums); j++ {
			if nums[j] > nums[i] {
				memo[i] = max(memo[i], 1+dp(j))
			}
		}

		return memo[i]
	}

	for i := range(nums) {
		res = max(res, dp(i))
	}

	return res
}

// Tabulation solution O(n^2) time: O(n) space
func lengthOfLISTab(nums []int) int {
	if len(nums) <= 0 {
		return 0
	}
	var res = 1
	tab := []int{}

	for i := range(nums) {
		tab = append(tab, 1)

		for j := i-1; j >= 0; j-- {
			if nums[i] > nums[j] {
				tab[len(tab)-1] = max(tab[len(tab)-1], 1 + tab[j])
				res = max(res, tab[len(tab)-1])
			}
		}

	}

	fmt.Println(tab)

	return res
}

func main() {
	//fmt.Println(lengthOfLISTab([]int{9,1,4,2,3,3,7}))
	fmt.Println(lengthOfLISTab([]int{1,3,6,7,9,4,10,5,6}))
	//fmt.Println(lengthOfLIS([]int{1,2,3}))
}
