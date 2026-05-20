'''
You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
'''

class Solution:
    def combinationSum2_forLoop(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

                # NOTE
                # You don't need to call backtrack again here (like you would in the below method)
                # Because you are in a for loop, next iteration already includes the fact that the prior iterations
                # subset has the skip case (worded pretty poorly)
                # Add the below line and see what happens
                # dfs(i + 1, path, cur)

        dfs(0, [], 0)
        return res

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

print(sol.combinationSum2_forLoop(candidates, target))
