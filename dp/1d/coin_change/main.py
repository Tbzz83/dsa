'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
'''

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dp(amt: int) -> int|float:
            if amt == 0:
                return 0
            if amt < 0:
                # Not possible
                return float('inf')

            if amt not in memo:
                res = float('inf')
                for coin in coins:
                    amt_needed = 1 + dp(amt-coin)
                    res = min(res, amt_needed)

                memo[amt] = res

            return memo[amt]
        
        res = dp(amount)
        
        return -1 if res == float('inf') else int(res)

    def coinChange_backtrack(self, coins: list[int], amount: int) -> int:
        res = float('inf')

        def backtrack(amt: int, iters: int):
            if amt == 0:
                nonlocal res
                res = min(res, iters)
                return
            if amt < 0:
                return

            for coin in coins:
                # Pick
                backtrack(amt - coin, iters + 1)

        backtrack(amount,0)

        return -1 if res == float('inf') else int(res)

sol = Solution()

print(sol.coinChange_backtrack([1,5,10], 12))
print(sol.coinChange([1,5,10], 12))
