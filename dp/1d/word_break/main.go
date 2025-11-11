package main

import (
	"fmt"
)

/*
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
*/

// Backtracking solution first
// time limit exceeded
func wordBreakBacktrack(s string, wordDict []string) bool {

	var backtrack func(i int, substr string) bool
	wordSet := make(map[string]bool)

	for _, str := range(wordDict) {
		wordSet[string(str)] = true
	}

	fmt.Println(wordSet)

	backtrack = func(i int, substr string) bool {
		fmt.Println(substr, i)
		if i == len(substr) {
			// substr non-empty
			_, ok := wordSet[substr[:i]]
			return ok
		}

		option1 := false

		if _, ok := wordSet[substr[:i]]; ok {
			option1 = backtrack(1, substr[i:])
		}

		if option1 { return true }

		option2 := backtrack(i+1, substr)

		return option2
	}

	return backtrack(0, s)
}

// DP solution using memoization
func wordBreak(s string, wordDict []string) bool {

	var dpFunc func(i int, substr string) bool
	wordSet := make(map[string]bool)
	dp := make(map[string]bool)

	for _, str := range(wordDict) {
		wordSet[string(str)] = true
	}

	dpFunc = func(i int, substr string) bool {
		if _, ok := wordSet[substr]; ok {
			dp[substr] = true
			return true
		} 
		if i > len(substr) {
			cond := false
			if substr == "" {
				cond = true
			}
			dp[substr] = cond
			return cond
		}

		if _, ok := dp[substr]; ok {
			return dp[substr]
		}

		valid := false
		// word exists
		if _, ok := wordSet[substr[:i]]; ok {
			fmt.Println("HI")
			valid = dpFunc(1, substr[i:])
			if valid {
				dp[substr] = valid
			}
		}

		if !valid {
			dp[substr] = dpFunc(i+1, substr)
		}

		return dp[substr]
	}

	return dpFunc(0, s)
}

func main() {
	s:="aaaaa"
	wordDict:=[]string{"aa","aaa"}

	fmt.Println(wordBreak(s, wordDict))
}
