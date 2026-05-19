
import copy

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        def backtrack(i: int, subset: list[int]):
            print(subset)
            if i >= len(nums):
                res.append(subset.copy())
                return

            # pick
            subset.append(nums[i])
            backtrack(i+1, subset)

            # skip
            subset.pop()
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            backtrack(j, subset)
        backtrack(0, [])

        return res

sol = Solution()
nums = [1,2,1]

print(sol.subsetsWithDup(nums))
#assert sol.subsetsWithDup(nums), [[],[1],[1,2],[1,1],[1,2,1],[2]]
