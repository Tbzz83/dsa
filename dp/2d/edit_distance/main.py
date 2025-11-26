# You are given two strings word1 and word2, each consisting of lowercase English letters.
# 
# You are allowed to perform three operations on word1 an unlimited number of times:
# 
#     Insert a character at any position
#     Delete a character at any position
#     Replace a character at any position
# 
# Return the minimum number of operations to make word1 equal word2.
# 
# Example 1:
# 
# Input: word1 = "monkeys", word2 = "money"
# 
# Output: 2


from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        len_1, len_2 = len(word1), len(word2)

        @cache
        def dp(i1, i2) -> int:
            if i2 >= len_2:
                return len_1 - i1

            elif i1 >= len_1:
                return len_2 - i2

            match = word1[i1] == word2[i2]
            if match:
                return dp(i1+1, i2+1)

            ins = 1 + dp(i1, i2+1)
            delete = 1 + dp(i1+1, i2)
            repl = 1 + dp(i1+1, i2+1)

            return min(ins, delete, repl)

        return dp(0,0)

def main():
    sol = Solution()
    print(sol.minDistance("ass", "as"))

if __name__ == "__main__":
    main()
