'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
'''


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}
        def dp(i: int, amt: int) -> int:
            if amt == 0:
                memo[(i,amt)] = 1
                return memo[(i,amt)]

            elif amt < 0 or i >= len(coins):
                return -1
            return memo[(i,amt)]

        res = dp(0,amount)
        print(memo)
        return res

sol = Solution()

print(sol.coinChange([1,5,10], 12))
