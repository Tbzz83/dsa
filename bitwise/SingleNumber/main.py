'''
https://neetcode.io/problems/missing-number/question?list=neetcode150
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

'''

class Solution:
    def missingNumber(self,nums: list[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n+1):
            if i == n:
                res ^= i
                break
            res ^= nums[i] ^ i

        return res

def main():
    res = 0
    nums = [0,1,2,4,5]
    sol = Solution()
    print(sol.missingNumber(nums))

if __name__ == "__main__":
    main()
