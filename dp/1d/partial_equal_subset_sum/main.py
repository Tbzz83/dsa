'''
https://neetcode.io/problems/partition-equal-subset-sum/question?list=neetcode150

You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.



nums = [1,2,3,4]
sum = sum(nums) = 10

target = sum / 2

subproblem: 
    - Is there a subarray in nums where sum(subarray) == target?

start at i = 0

choices:
num = nums[i] = nums[0] = 1
    1. pick num
        target -= num
    2. skip num
        target = target
'''


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        memo = {}

        nums_sum = sum(nums)

        if nums_sum % 2 > 0:
            return False

        target = int(nums_sum // 2)


        def dp(i: int, t: int) -> bool:
            if t == 0:
                return True
            elif t < 0 or i >= len(nums):
                return False

            key = (i,t)

            if key not in memo:
                memo[key] = dp(i+1, t) or dp(i+1, t-nums[i])

            return memo[key]
        
        res = dp(0, target)

        return res


sol = Solution()

nums = [1,2,3,4,5]
print(sol.canPartition(nums))
