'''
You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
'''

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        candidates.sort()

        def backtrack(i: int, subset: list[int], cur_sum: int):
            if cur_sum == target:
                res.append(subset.copy())
                return
            elif i >= len(candidates) or cur_sum > target:
                return

            # Pick
            subset.append(candidates[i])
            backtrack(i+1, subset, cur_sum + candidates[i])
            subset.pop()

            # Skip
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            backtrack(j, subset, cur_sum)

        backtrack(0, [], 0)
        return res


candidates = [9,2,2,4,6,1,5]
target = 8

sol = Solution()

print(sol.combinationSum2(candidates, target))
