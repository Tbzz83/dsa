'''
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

    For example, "cat" is a subsequence of "crabt".

A common subsequence of two strings is a subsequence that exists in both strings.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def dp(i: int, j: int) -> int: 
            if i >= len(text1) or j >= len(text2):
                return 0

            key = (i,j)

            if key not in memo:
                l,r = text1[i], text2[j] 
                if l == r:
                    # match
                    # must increment both
                    memo[key] = 1 + dp(i+1, j+1)
                else:
                    memo[key] = max( dp(i+1,j+1) , dp(i,j+1), dp(i+1,j))

            return memo[key]

        return dp(0,0)

text1 = "cat"

text2 = "crabt"

text1 = "bsbininm"
text2 = "jmjkbkjkv"

sol = Solution()

print(sol.longestCommonSubsequence(text1, text2))
