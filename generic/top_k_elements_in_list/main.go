package main

import (
	"fmt"
	"sort"
)

func topKFrequent(nums []int, k int) []int {
	var res []int
	var counts = make(map[int]int)

	keys := make([]int, 0, len(counts))
	for k2 := range counts {
		keys = append(keys, k2)
	}
	

	for _, val := range(nums) {
		counts[val] += 1
	}

	fmt.Println(counts)

	return res
}


func main() {
	res := topKFrequent([]int{1,1,1,2,2,3}, 2)
	fmt.Println(res)
}
