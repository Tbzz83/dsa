package main

import (
  "fmt"
)

// TODO
// Error messages

type Bucket struct {
  // TODO
  // Enums for different types of Keys and Values
  Key string
  Value string
  Next *Bucket
}

type HashTable struct {
  /*
  Use a slice of pointers because we may need to
  update a bucket in place. 
  */
  Buckets []*Bucket
  size int
}

func (h *HashTable) del(key string) {
  hash := hashFunction(key)
  trueHash := hash % h.size

  cur := h.Buckets[trueHash]
  if cur != nil {
    if cur.Key == key {
      // We want to remove first node of ll
      h.Buckets[trueHash] = cur.Next
      cur = nil
      return
    } else {
      next := cur.Next
      for next != nil {
        // We want to remove some other element of the ll
        if next.Key == key {
          cur.Next = next.Next
          next = nil
          return
        }
        cur = cur.Next
        next = next.Next
      }
    }
  }
  fmt.Println("Key error. Key:", key, "does not exist in the hash table.")
  return
}

func (h *HashTable) handleCollision(newBucket *Bucket, trueHash int) {
  existingBucket := h.Buckets[trueHash]
  if newBucket.Key == existingBucket.Key {
    fmt.Println("Key. Key", newBucket.Key, "already exists in hash table.")
    return
  }

  // Get to end of linked list
  for existingBucket.Next != nil {
    fmt.Println("Iterating through collided buckets...")
    if newBucket.Key == existingBucket.Key {
      fmt.Println("Key error. Key", newBucket.Key, "already exists in hash table.")
      return
    }
    // Make sure key doesn't already exist
    existingBucket = existingBucket.Next
  }
  existingBucket.Next = newBucket
}

func (h *HashTable) getValue(key string) string {
  hash := hashFunction(key)
  trueHash := hash % h.size
  curBucket := h.Buckets[trueHash]
  for curBucket != nil {
    if curBucket.Key == key {
      return curBucket.Value
    }
    curBucket = curBucket.Next
  }
  fmt.Println("Key error: Key:", key, "does not exist in hash map")
  return ""
}

func (h *HashTable) insert(key string, value string) {
  hash := hashFunction(key)
  trueHash := hash % h.size
  fmt.Println("Inserting key:", key, "with value:", value, "into hash table")
  fmt.Println("Key hash:", hash)
  newBucket := createBucket(key, value)

  if h.Buckets[trueHash] == nil {
    h.Buckets[trueHash] = newBucket
    fmt.Println("New bucket added:",*h.Buckets[trueHash])
  } else {
    // Collision occured
    fmt.Println("Collision occured with hash:", trueHash, "and key:", key)
    h.handleCollision(newBucket, trueHash)
  }
}

func createBucket(key string, value string) *Bucket {
  var bucket Bucket
  bucket.Key = key
  bucket.Value = value
  return &bucket
}

func createHashTable(size int) *HashTable {
  var h HashTable
  buckets := make([]*Bucket, size, size)
  h.Buckets = buckets
  h.size = size
  return &h
}

func hashFunction(wordKey string) int {
  var res int
  for _, v := range(wordKey) {
    res += int(v)
  }
  return res
}

func (h *HashTable) printHashTable() {
  fmt.Println("{")
  for i := range(h.Buckets) {
    if h.Buckets[i] != nil {
      fmt.Print(" ", h.Buckets[i].Key, " : ", h.Buckets[i].Value, ",")
      fmt.Println()
    }
  }
  fmt.Println("}")
}

