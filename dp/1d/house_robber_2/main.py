'''
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}

        def dp(i: int, max_len: int) -> int:
            if i >= max_len:
                return 0

            if i not in cache:
                rob = nums[i] + dp(i+2, max_len) 
                skip = dp(i+1, max_len)
                cache[i] = max(rob, skip)

            return cache[i]

        a = dp(0, len(nums)-1)
        cache = {}
        b = dp(1,len(nums))

        return max(a,b)

        


sol = Solution()
nums = [2,3,2]
nums=[2,9,8,3,6]

print(sol.rob(nums))
