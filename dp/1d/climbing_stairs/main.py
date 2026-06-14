'''
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dp(i: int) -> int:
            if i == n:
                return 1
            elif i > n:
                return 0

            if i not in memo:
                memo[i] = dp(i+1) + dp(i+2)

            return memo[i]

        res = dp(0)

        print(memo)

        return res

            


n = 6

sol = Solution()
print(sol.climbStairs(n))
