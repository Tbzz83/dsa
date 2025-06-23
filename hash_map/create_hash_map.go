package main

import (
  "fmt"
)


func HashMap() {
  // ----
  fmt.Println()
  fmt.Println("----Hash Map with Go----")
  hSize := 10 // 10 buckets 
  h := createHashTable(hSize)
  h.insert("myKey", "myValue")
  h.insert("otherKey", "otherValue")
  fmt.Println()
  fmt.Println("Hash table:")
  h.printHashTable()

  invalidKey := h.getValue("INVALID")
  fmt.Println(invalidKey)
  fmt.Println("deleting 'myKey' from hash table")
  h.del("oweifn")
  h.printHashTable()


  fmt.Println("------------------------")
}

