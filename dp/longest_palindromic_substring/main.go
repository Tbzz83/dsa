package main

import "fmt"


func longest(s string) string {

  resL := -1
  resR := -1


  for i := range(s) {
    fmt.Println(s[i])

  }

  return 
}

func main() {

  fmt.Println(longest("babad"))
  fmt.Println(longest("cbbd"))

}
