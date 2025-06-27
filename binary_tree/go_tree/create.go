package main

import (
  "fmt"
  "os"
  "bufio"

)


func BuildCustomTree() {
  /* 
  User input based implementation for creating any type of tree 
  valid or invalid!
  */

  var levels int
  for {
    fmt.Print("Enter a number of levels for the tree:")
    _, err := fmt.Scan(&levels)
    if err != nil {
    } else {
      break
    }
  }
  fmt.Println("Levels entered are:", levels)

  res = append()

  reader := bufio.NewReader(os.Stdin)
  fmt.Print("Enter in some text: ")
  text, err := reader.ReadString('\n')
  if err != nil {
    fmt.Println("error occurred")
    return
  }

  fmt.Println(text)

}
