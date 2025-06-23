package main

import (
  "fmt"
)

type WordDictionary struct {
  Val string
  Children [26]*WordDictionary
  Eow bool
}

func Constructor() WordDictionary {
  res := WordDictionary{}
  return res
}

func (this *WordDictionary) AddWord(word string) {
  fmt.Printf("Adding word %q to WordDictionary\n", word)
  for _, v := range(word) {
    arrI := v - 'a'
    if this.Children[arrI] != nil {
      this = this.Children[arrI]
    } else {
      this.Children[arrI] = &WordDictionary{Val: string(v), Eow: false}
      this = this.Children[arrI]
    }
  }
  this.Eow = true
}

func (this *WordDictionary) Search(word string) bool {
  for i, v := range(word) {
    arrI := v - 'a'
    if string(v) == "." {
      for _, v := range(this.Children) {
        if v != nil && v.Search(word[i+1:]) {
          return true
        }
      }
      return false
    } else if this.Children[arrI] != nil {
      this = this.Children[arrI]
    } else {
      return false
    }
  }
  return this.Eow
}
