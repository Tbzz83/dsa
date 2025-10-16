# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
#
# We want to run a simulation on the stones as follows:
#
#    At each step we choose the two heaviest stones, with weight x and y and smash them togethers
#    If x == y, both stones are destroyed
#    If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#
# Continue the simulation until there is no more than one stone remaining.
#
# Return the weight of the last remaining stone or return 0 if none remain.
#
# Example 1:
#
# Input: stones = [2,3,6,2,4]
#
# Output: 1
#
# Explanation:
# We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
# We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
# We smash 2 and 2, so the array becomes [1].
#
# Example 2:
#
# Input: stones = [1,2]
#
# Output: 1
#
# Need to compare the TWO largest items in the array
# while len(arr) > 1: fight()
# fight(x, y) are the stone weights. if x == y both stones are removed
# if x > y, x = x - y, y is removed
#
# Can use a max heap to represent this.
#
# fight can be a function that returns an array of all new values to be added from the
# max heap. Every fight, BOTH of x and y WILL have to be removed regardless. If x wins, it's
# value will be reassigned (as y cannot == 0), so will have to remove it and reinsert it.
#
# Heaviest stone will be found at arr[0]. Second heaviest can be found by searching for 2*0 + 1 and 2*0 + 2 and comparing them to see which is larger. (which is the larger child)

import heapq


def lastStoneWeight(stones: list[int]) -> int:
    # Negate value of stones
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        print(stones)
        largest = heapq.heappop(stones)  # pop largest
        second_largest = heapq.heappop(stones)  # pop second largest

        diff = largest - second_largest

        if diff != 0:
            heapq.heappush(stones, -abs(diff))

    if len(stones) > 0:
        return -stones[0]
    else:
        return 0


def main():
    print(lastStoneWeight([2, 3, 6, 2, 4]))
    print(lastStoneWeight([1, 2]))


if __name__ == "__main__":
    main()
