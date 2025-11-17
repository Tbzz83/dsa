# You are given an array of integers nums and an integer target.
# 
# For each number in the array, you can choose to either add or subtract it to a total sum.
# 
#     For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
# 
# If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".
# 
# Return the number of different ways that you can build the expression such that the total sum equals target.
#
# NOTES
# Have to use every number in nums
# 
# Effectively, we either multiply num by 1 or -1, then add it to our total sum, and continue
# from next index
#
# Only need to visit every number once


from collections import defaultdict
class Solution:
    # Top down memoiz
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cache: dict[tuple[int, int], int] = defaultdict(int)

        def dp(i: int, target: int) -> int:
            if i >= len(nums):
                if target == 0:
                    return 1
                return 0

            if not (i, target) in cache:
                cache[(i, target)] = dp(i+1, target+nums[i]) + dp(i+1, target-nums[i])

            return cache[(i, target)]

        return dp(0, target)

def main():
    nums = [2,2,2]
    target = 2
    sol = Solution()
    print(sol.findTargetSumWays(nums, target))

if __name__ == "__main__":
    main()
