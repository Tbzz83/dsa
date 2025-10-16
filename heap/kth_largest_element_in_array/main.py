# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
#
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
#
# Follow-up: Can you solve it without sorting?
#
# Example 1:
#
# Input: nums = [2,3,1,5,4], k = 2
#
# Output: 4
#
# Example 2:
#
# Input: nums = [2,3,1,1,5,5,4], k = 3
#
# Output: 4
#
# Constraints:
#
#    1 <= k <= nums.length <= 10000
#    -1000 <= nums[i] <= 1000
#
# We need to return the kth largest element in sorted order from input nums
#
# We can iterate through the array and simultaneously build a min heap.
# We only push values into our min heap that are greater than the min value, if len(min_heap) < k

import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    min_heap = []

    for num in nums:
        if len(min_heap) < k or num > min_heap[0]:
            heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


def main():
    print(findKthLargest([2, 3, 1, 1, 5, 5, 4], 3))


if __name__ == "__main__":
    main()
