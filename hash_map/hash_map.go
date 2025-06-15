package hash_map

import (
  "fmt"
)


func HashMap() {
  // ----
  hSize := 10 // 10 buckets 
  h := createHashTable(hSize)
  h.insert("myKey", "myValue")
  h.insert("otherKey", "otherValue")
  fmt.Println()
  fmt.Println("Hash table:")
  h.printHashTable()

  testValue := h.getValue("fewoinfew")
  fmt.Println(testValue)
}

