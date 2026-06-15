package main

import (
)

func maxDepth(node *treeNode) int {
  if node == nil {
    return 0
  }

  return 1 + max(maxDepth(node.Left), maxDepth(node.Right))
}

func goodNodes(node *treeNode) int {
  if node == nil {
    return 0
  }
  count := 0
  goodNodesDfs(node, node.Val, &count)
  return count
}

func invertTree(node *treeNode) {
	if node == nil {
		return
	}

	tmp := node.Right
	node.Right = node.Left
	node.Left = tmp

	invertTree(node.Right)
	invertTree(node.Left)
}

func goodNodesDfs(node *treeNode, maxi int, count *int) {
  if node == nil {
    return
  }

  if node.Val >= maxi {
    *count ++
    maxi = node.Val
  }

  goodNodesDfs(node.Left, maxi, count)
  goodNodesDfs(node.Right, maxi, count)
}
