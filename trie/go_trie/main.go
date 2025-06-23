package main

import (
  "fmt"
)

func main() {
  obj := Constructor()
  word := "hello"
  fmt.Println(obj)
  obj.AddWord(word)
  fmt.Println(obj.Search("hello"))

}

