# Given an array of integers nums, find the subarray with the largest sum and return the sum.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# NOTES
# Consider: nums = [2,-3,4,-2,2,1,-1,4]
# We can do this in O(n) using a running total. 
# If a value brings our total to <= 0, we should reset the counter.
# This also means if an array contains all negative values, 
# the max subarray will always be of length 1. Two negative
# numbers added together can never be greater than just one of them.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        global_max = nums[0]
        cur_max = 0

        for r in range(len(nums)):
            num = nums[r]
            cur_max += num
            global_max = max(global_max, cur_max)
            cur_max = 0 if cur_max <= 0 else cur_max

        return global_max

def main():
    print("---max subarray---")
    #nums = [2,-3,4,-2,2,1,-1,4]
    nums = [-2,1]
    sol = Solution()

    print(sol.maxSubArray(nums))

    

if __name__ == "__main__":
    main()
