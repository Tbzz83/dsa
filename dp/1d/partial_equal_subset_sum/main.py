'''
https://neetcode.io/problems/partition-equal-subset-sum/question?list=neetcode150

You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.
'''


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 > 0:
            return False

        memo = {}

        target = int(total/2)
        def dp(i: int, cur_sum: int) -> bool:
            print(i, cur_sum, target)
            if cur_sum > target:
                return False
            if cur_sum == target:
                return True
            if i >= len(nums):
                return cur_sum == target

            num = nums[i]

            if cur_sum not in memo:
                # pick
                pick = dp(i+1, cur_sum + num)
                # skip
                skip = dp(i+1, cur_sum)
                memo[cur_sum] = pick or skip
            else:
                print("Cache hit")

            return memo[cur_sum]

        res = dp(0, 0)
        print(memo)

        return res

sol = Solution()

nums = [1,2,3,4]
print(sol.canPartition(nums))
        
