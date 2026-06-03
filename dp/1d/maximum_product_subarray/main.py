class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return -1

        res = nums[0]

        prev_min, prev_max = 1,1

        for num in nums:
            cur_min, cur_max = min(num, num*prev_min, num*prev_max), max(num, num*prev_min, num*prev_max)
            res = max(res, cur_max)
            prev_min, prev_max = cur_min, cur_max

        return res

    # Backtrack
    def maxProductBacktrack(self, nums: list[int]) -> int:
        if not nums:
            return -1

        res = nums[0]

        def backtrack(i: int):
            if i >= len(nums):
                return

            nonlocal res
            tot = nums[i]
            res = max(res, tot)

            for j in range(i+1, len(nums)):
                print(i,j,tot)
                tot *= nums[j]
                res = max(res, tot)

            backtrack(i+1)

        backtrack(0)

        return res

sol = Solution()
nums = [-2,-1]
#nums = [1,2,-3,4,3,4,4,5,7,-1,2,3,-11]
nums = [-3,-1,-1]
nums = [1,2,-3,4]

print(sol.maxProduct(nums))
