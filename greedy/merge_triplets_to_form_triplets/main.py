'''
You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

To obtain target, you may apply the following operation on triplets zero or more times:

Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
* E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

Return true if it is possible to obtain target as an element of triplets, or false otherwise.
'''

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target

        triplets.sort()

        def merge(trip_i: list[int], trip_j: list[int]) -> list[int]:
            return [
                max(trip_i[0], trip_j[0]),
                max(trip_i[1], trip_j[1]),
                max(trip_i[2], trip_j[2]),
            ]

        def is_valid(triplet: list[int]) -> bool:
            return (triplet[0] <= target[0] and
                    triplet[1] <= target[1] and
                    triplet[2] <= target[2]
                    )

        cur = triplets[0]

        for i in range(len(triplets)-1,0,-1):
            if not is_valid(cur):
                cur = triplets[i]
                continue

            candidate = merge(cur,triplets[i])

            if is_valid(candidate):
                cur = candidate

            if cur == target:
                return True

        return False
        
sol = Solution()
triplets = [
    [1,2,3],
    [7,1,1],
]
triplets = [[2,5,6],[1,4,4],[5,7,5]]
target = [7,2,3]

triplets=[[4,5,2],[4,2,7],[5,8,6],[3,6,6],[4,5,2]]
target=[4,5,7]

print(sol.mergeTriplets(triplets, target))
