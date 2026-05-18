'''
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
'''

import copy

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(i: int, subset: list[int]):
            if i >= len(nums):
                clone = copy.deepcopy(subset)
                res.append(clone)
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop(len(subset)-1)
            backtrack(i+1, subset)

        backtrack(0, [])
        return res

sol = Solution()
nums = [1,2,3]
assert sol.subsets(nums),  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
