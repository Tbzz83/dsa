# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# 
# You may buy and sell one NeetCoin multiple times with the following restrictions:
# 
#     After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
#     You may only own at most one NeetCoin at a time.
# 
# You may complete as many transactions as you like.
# 
# Return the maximum profit you can achieve. 
#
# Notes:
# We can only hold one coin at a time. We pay prices[i] price for it. we sell if for prices[i] on whatever
# day (today or in the future). Can't sell for a prior day, obv
#
# IF we sell, we must skip the next day. Can't buy on the same day we sell.
# 
# Constraints:
# 
#     1 <= prices.length <= 5000
#     0 <= prices[i] <= 1000
# 

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo: dict[tuple[int, bool], int] = {}

        def dp(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                res = dp(i+1, not buying) - prices[i]

            else:
                res = dp(i+2, not buying) + prices[i]

            cooldown = dp(i+1, buying)
            memo[(i, buying)] = max(cooldown, res)
            return memo[(i, buying)]
        return dp(0, True)
                
def main():
    sol = Solution()
    print(sol.maxProfit([1,2,3,4]))

if __name__ == "__main__":
    main()
