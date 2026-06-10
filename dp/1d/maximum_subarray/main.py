
'''
Given an integer array nums, find the subarray
with the largest sum, and return its sum.
https://leetcode.com/problems/maximum-subarray/
A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        maxi = nums[0]
        cur_sum = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            maxi = max(maxi, cur_sum)
        return maxi


nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
#nums = [5,4,-1,7,8]
#nums = [-11,-2,-6,-1]

sol = Solution()

print(sol.maxSubArray(nums))
