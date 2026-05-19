'''
You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
'''

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack():
            pass

        return res


candidates = [9,2,2,4,6,1,5]
target = 8

sol = Solution()

print(sol.combinationSum2(candidates, target))
