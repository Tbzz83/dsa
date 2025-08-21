package main

import "fmt"

func topKFrequent(nums []int, k int) []int {

  var counts = make(map[int]int)
  var buckets = make([][]int, len(nums)+1)

  fmt.Println(buckets)

  var res []int

  for _, val := range(nums) {
    counts[val]++
  }

  // populate buckets with counts
  for num, count := range(counts) {
    buckets[count] = append(buckets[count], num)
  }

  // iterate backward through bucketss
  for i := len(buckets) - 1; i > 0 && k > 0; i-- {
    bucket := buckets[i]

    if len(bucket) == 0 {continue}

    for _, val := range(bucket) {
      if k == 0 {break}
      res = append(res, val)
      k--
    }
  }

  return res
  
}


func main() {

  //res := topKFrequent([]int{1,1,1,2,2,3}, 2)
  res := topKFrequent([]int{1}, 1)
  fmt.Println(res)
}
