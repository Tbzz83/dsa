package main

import (
  "fmt"
)


func main() {
  fmt.Println("===Binary Tree With Go===")
  preorder := []int {3,2,20,15,21,}
  root := buildFromPreorder(preorder)
  fmt.Println("root:", root)
  printPreorder(root)
  printLevel(root)
  fmt.Println("\nMax depth of binary tree is:", maxDepth(root))
  fmt.Println("\nNumber of good nodes in binary tree is:", goodNodes(root))
  fmt.Println()
  BuildCustomTree()


	fmt.Println()
}
