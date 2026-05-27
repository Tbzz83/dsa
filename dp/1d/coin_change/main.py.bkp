'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

[2,3], target = 5


'''

from functools import cache


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dfs(i: int, amt: int) -> int:
            if i >= len(coins):
                return 0 if amt == 0 else -1

            if amt not in memo:
                take = 0
                if coins[i] <= amt:
                    take = dfs(i, amt-coins[i])
                skip = dfs(i+1, amt)
                memo[amt] = min(take,skip)
            return memo[amt]

        ans = dfs(0,amount)
        print(memo)
        return ans

def main():
    sol = Solution()
    coins = [1,3]
    print(sol.coinChange(coins, 4))

if __name__ == "__main__":
    main()
