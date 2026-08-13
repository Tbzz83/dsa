'''
https://neetcode.io/problems/missing-number/question?list=neetcode150

Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



EXAMPLE

        
nums = [0,2] ~ nums = [00, 10]

000
001
010
011
100

find out the largest number in the array
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        largest = nums[0]

        for num in nums:
            largest = max(largest, num)

        print(largest)

        copy = largest

        max_bin_len = largest.bit_length()

        print(f"bin length for {bin(largest)} is {max_bin_len}")

        max_poss_value = 0
        for i in range(max_bin_len):
            max_poss_value = max_poss_value | 1 << i

        res = nums[0]

        for num in nums[1:]:
            print(bin(num))
            res |= num

        print(bin(res))

sol = Solution()

nums = [1,2,3,5]

print(sol.missingNumber(nums))
