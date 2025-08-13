package main

import ( 
  "fmt"
)

type ListNode struct {
  Val int
  Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
  if right == left {return head}
  head = &ListNode{Next: head}
  cur := head
  prev := cur
  idx := 0 // 1-indexed because we start before the head

  // Get to left node
  for cur != nil && idx != left {
    prev = cur
    cur = cur.Next
    idx ++
  }

  before := prev
  after := cur

  prev = nil
  fmt.Println("idx:", idx)
  for cur != nil && idx <= right {
    if idx == right {
      after.Next = cur.Next
    }

    tmp := cur.Next
    cur.Next = prev
    prev = cur
    cur = tmp
    idx++
  }

  before.Next = prev
  fmt.Println(before, before.Next)
  fmt.Println(head.Next)

  return head.Next
}

func build(arr []int) *ListNode {
  var head *ListNode
  var cur *ListNode
  for i, v := range(arr) {
    if i == 0 {
      head = &(ListNode{Val: v})
      cur = head
      continue
    }

    cur.Next = &(ListNode{Val: v})
    cur = cur.Next
  }

  return head
}

func printList(head *ListNode) {
  fmt.Println()
  fmt.Println("Printing linked list...")
  cur := head
  for cur != nil {
    fmt.Println(cur.Val)
    cur = cur.Next
  }
}


func main() {
  head := build([]int{3,5})
  head = reverseBetween(head, 1,2)
  printList(head)

}
