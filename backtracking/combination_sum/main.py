'''
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.


no dups
'''

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(i: int, cur_sum: int, subset: list[int]):
            if cur_sum == target:
                res.append(subset.copy())
                return
            elif cur_sum > target or i >= len(nums):
                return

            # Pick
            subset.append(nums[i])
            backtrack(i, cur_sum + nums[i], subset)

            # Skip
            subset.pop()
            backtrack(i+1, cur_sum, subset)

        backtrack(0, 0, [])

        return res

nums = [2,5,6,9]
target = 9 
sol = Solution()

print(sol.combinationSum(nums, target))
