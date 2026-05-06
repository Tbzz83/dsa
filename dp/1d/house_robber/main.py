# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
# 
# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
# 
# Return the maximum amount of money you can rob without alerting the police.

class Solution:
    def rob(self, nums: list[int]) -> int:
        # keys are idx, vals are max you can rob from this idx forward
        memo: dict[int,int] = {}
        memo[len(nums)-1] = nums[len(nums)-1]

        def dp(i: int) -> int:
            if i >= len(nums):
                return 0

            if i not in memo:
                pick = nums[i] + dp(i+2)
                skip = dp(i+1)

                memo[i] = max(pick, skip)

            return memo[i]

        return dp(0)


    def rob_backtrack(self, nums: list[int]) -> int:
        total = 0
        def backtrack(i: int, cur_tot: int):
            if i >= len(nums):
                nonlocal total
                total = max(total, cur_tot)
                return
            
            cur_house = nums[i]
            pick = cur_tot + cur_house
            backtrack(i+2, pick)
            backtrack(i+1, cur_tot)

        backtrack(0,0)
        return total
        

def main():
    sol = Solution()
    assert sol.rob([1,1,3,3]) == 4
    assert sol.rob([2,9,8,3,6]) == 16

if __name__ == "__main__":
    main()
