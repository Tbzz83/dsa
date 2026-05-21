'''
Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

'''

class Solution:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            l_char, r_char = s[l], s[r]

            if l_char != r_char:
                return False

            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> list[list[str]]:
        
        res = []

        def backtrack(l: int, r: int, substr: list[str]):
            if l == len(s):
                res.append(substr.copy())
                return
            if r > len(s):
                return

            
            split = s[l:r]
            if self.is_palindrome(split):
                substr.append(split)
                backtrack(r,r+1,substr)
                substr.pop()

            backtrack(l,r+1,substr)
            
        backtrack(0, 1, [])

        return res
        
sol = Solution()

s = "aab"
print(sol.is_palindrome(s))

print(sol.partition(s))
