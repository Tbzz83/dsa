package main

import (
  "fmt"
)

func getRow(rowIndex int) []int {
  switch rowIndex {
  case 0:
    return []int{1}
  case 1:
    return []int{1,1}
  }

  parent := []int{1}

  for i := 1; i < rowIndex + 1; i++ {
    row := make([]int, i+1)
    row[0] = 1
    row[i] = 1

    pL := 0
    pR := 1

    for j := 1; j < i; j++ {
      row[j] = parent[pL] + parent[pR]
      pL++
      pR++
    }

    parent = row
  } 

  return parent
}

func main() {
  fmt.Println(getRow(5))

}
