package main

import (
  "fmt"
)

type treeNode struct {
  Val int
  Left *treeNode
  Right *treeNode
}

func buildFromPreorder(arr []int) *treeNode {
  if arr == nil {
    fmt.Println("Error creating tree: empty array.")
    return nil
  }

  // Create root node
  root := treeNode{arr[0], nil, nil}

  for _, val := range(arr[1:]) {
    newNode := treeNode{val, nil, nil}
    addNodeValidTree(&root, &newNode)
  }
  return &root
}

func addNodeValidTree(node *treeNode, newNode *treeNode) {
  if newNode.Val > node.Val {
    if node.Right != nil {
      addNodeValidTree(node.Right, newNode)
    } else {
      node.Right = newNode
    }
  } else if newNode.Val < node.Val {
    if node.Left != nil {
      addNodeValidTree(node.Left, newNode)
    } else {
      node.Left = newNode
    }
  } else {
    fmt.Printf("Error. New node has same value '%d' as noderent node '%d'\n", newNode.Val, node.Val)
    return 
  }
  return 
}

func printPreorder(node *treeNode) {
  if node == nil {
    return
  }

  fmt.Println(node.Val)
  printPreorder(node.Left)
  printPreorder(node.Right)

}

func printLevel(node *treeNode) {
  fmt.Println("\nPrinting BFS tree")
  q := make([]*treeNode, 1)
  q[0] = node
  
  i := 0
  for len(q) > 0 {
    fmt.Println("Level:", i)
    qLen := len(q)
    for i := range(qLen) {
      popped := q[0]
      if popped.Left != nil {
        q = append(q, popped.Left)
      }
      if popped.Right != nil {
        q = append(q, popped.Right)
      }
      fmt.Print(popped.Val)

      if i != qLen - 1 {
        // Won't print comma at end
        fmt.Print(",")
      }
      q = q[1:]
    }
    fmt.Printf("\n")
    i++
  }
}



