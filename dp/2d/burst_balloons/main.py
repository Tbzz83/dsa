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

# Our two states are pop, or don't pop basically
#
# 


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        pass

def main():
    sol = Solution()
    print(sol.maxCoins([4,2,3]))

if __name__ == "__main__":
    main()
