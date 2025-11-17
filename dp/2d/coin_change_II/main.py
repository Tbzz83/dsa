# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
# 
# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.
# 
# You may assume that you have an unlimited number of each coin and that each value in coins is unique.
#
# Two states
# 1. Index of coins 'i' that we are at
# 2. Target value we're searching for. 
#
# How our cache should look
# cache = {
#     index = {
#         target = number_of_combinations
#     }
# }

class Solution:
    def change_mem_optimized(self, amount: int, coins: list[int]) -> int:
        cache = [0] * (amount + 1)
        cache[len(cache)-1] = 1

        for coin in coins[::-1]:
            next_dp = [0] * (amount + 1)

            for i in range(len(next_dp) -1, -1, -1):
                next_dp[i] = cache[i] + (
                        next_dp[i+coin] if (i+coin) in range(len(next_dp)) else 0
                )
            cache = next_dp

        return cache[0]

    def change(self, amount: int, coins: list[int]) -> int:
        cache: dict = {}

        def dp(i: int, target: int) -> int:
            if i >= len(coins):
                return 0
            elif target == 0:
                if i not in cache:
                    cache[i] = {}
                    
                cache[i][target] = 1
                return 1

            elif target < 0:
                if i not in cache:
                    cache[i] = {}

                cache[i][target] = 0
                return 0

            if i in cache:
                idx_dict = cache[i]

                if target in idx_dict:
                    return idx_dict[target]

            else:
                cache[i] = {}

            cache[i][target] = dp(i, target-coins[i]) + dp(i+1, target)

            return cache[i][target]

        dp(0, amount)

        if 0 in cache and amount in cache[0]:
            return cache[0][amount]

        return 0
        
def main():
    amount = 3
    coins = [1,2]
    sol = Solution()

    print(sol.change_mem_optimized(amount, coins))


if __name__ == "__main__":
    main()
