"""
HARD: https://neetcode.io/problems/foreign-dictionary/question?list=neetcode150

There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

    The first letter where they differ is smaller in a than in b.
    a is a prefix of b and a.length < b.length.

"""

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        return ""

sol = Solution()

words = ["z","o"]

print(sol.foreignDictionary(words))

