package main

import (
  "fmt"
  "strconv"
)

func letterCombinations(digits string) []string {
    letters := new([10][]byte)
    fmt.Println("letters:", letters)

    var char byte = 97 // 'a' in ASCII
    for i:=2; i < len(letters) ; i++ {
        numChars := 3

        if i == 7 || i == 9 {
            numChars = 4
        }

        for range(numChars) {
          (*letters)[i] = append((*letters)[i], char)
          char++
        }
    }
    fmt.Println(letters)

    res := []string{}
    startingSubset := ""
    startingIdx := 0

    backtrack(&res, letters, startingSubset, digits, startingIdx)

    return res
}

func backtrack(res *[]string, letters *[10][]byte, subset, digits string, idx int) error {
  if idx > len(digits) - 1 {
    *res = append(*res, subset)
    return nil
  }

  lettersIdx, err := strconv.Atoi(string(digits[idx]))
  if err != nil {
    return err
  }

  charOptionSlice := (*letters)[lettersIdx]

  for _, c := range(charOptionSlice) {
    subset += string(c)
    backtrack(res, letters, subset, digits, idx+1)
    subset = subset[:len(subset)-1]
  }

  return nil
}

func main() {
  digits := "23"
  res := letterCombinations(digits) 
  fmt.Println(res)
}


