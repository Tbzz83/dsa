package hash_map 

import (
  "fmt"
)

type Bucket struct {
  Key int
  Value string
  Next *Bucket
}

type HashTable struct {
  Buckets []Bucket
}

func (h *HashTable) insert(key string, value string) {
  hash := hashFunction(key)
  if h[hash] != nil {
    //collision
  }

  //bucket := createBucket(key, value)



}

func createBucket(key int, value string) *Bucket {
  var bucket Bucket
  bucket.Key = key
  bucket.Value = value
  return &bucket
}

func createHashTable(size int) *HashTable {
  var h HashTable
  buckets := make([]Bucket, size, size)
  h.Buckets = buckets
  return &h
}

func hashFunction(wordKey string) {
  var res int
  for _, v := range(wordKey) {
    res += int(v)
  }
  return res
}
