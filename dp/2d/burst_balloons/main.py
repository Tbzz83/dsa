# You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.
# 
# If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.
# 
# Return the maximum number of coins you can receive by bursting all of the balloons.
# 
# Example 1:
# 
# Input: nums = [4,2,3,7]
# 
# Output: 143
# 
# Explanation:
# nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
# coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] +  nums + [1]
        dp = {}

        def dfs(l,r) -> int:
            if l > r:
                return 0

            if (l,r) in dp:
                return dp[(l,r)]

            dp[(l,r)] = 0
            for i in range(l,r + 1):
                coins = nums[i] * nums[r+1] * nums[l-1]
                coins += dfs(l,i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[l,r], coins)

            return dp[(l,r)]

        return dfs(1, len(nums) -2)

def main():
    sol = Solution()
    print(sol.maxCoins([4,2,3,7]))

if __name__ == "__main__":
    main()
