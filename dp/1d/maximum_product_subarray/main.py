class Solution:
    # DP Memoization
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return -1

        memo: dict[int, tuple[int,int]] = {}
        res = nums[0]

        # Return max of all subarrays starting from this i
        def dp(i: int) -> tuple[int,int]:
            if i >= len(nums):
                return 1,1

            if i not in memo:
                next_min, next_max = dp(i+1)
                num = nums[i]
                cur_min = min(num*next_min, num*next_max, num)
                cur_max = max(num*next_min, num*next_max, num)

                nonlocal res
                res = max(res, cur_max)

                memo[i] = (cur_min, cur_max)

            else:
                print("CASE")

            return memo[i]

        dp(0)[1]
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
nums = [-3,-1,-1]
nums = [1,2,-3,4,3,4,4,5,7,-1,2,3,-11]

print(sol.maxProduct(nums))
