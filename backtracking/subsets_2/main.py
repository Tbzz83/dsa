# Given an integer array nums that may contain duplicates, return all possible (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subsets: list[list[int]] = []
        def backtrack(idx: int, subset: list[int]):
            if idx >= len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[idx])
            backtrack(idx+1, subset)
            subset.pop()
            while idx+1 < len(nums) and nums[idx+1] == nums[idx]:
                idx += 1
            backtrack(idx+1, subset)
        backtrack(0, [])
        return subsets

def main():
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2,3]))

if __name__ == "__main__":
    main()
