class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []

        def backtrack(i: int):
            if i >= len(nums) -1:
                res.append(nums.copy())
                return

            for j in range(i,len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return res


nums = [1,2,3]
sol = Solution()

print(sol.permute(nums))
