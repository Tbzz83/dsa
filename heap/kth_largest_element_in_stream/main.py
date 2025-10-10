#Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
#
#Implement the following methods:
#
#    constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
#    int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
#
#Example 1:
#
#Input:
#["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
#
#Output:
#[null, 3, 3, 3, 5, 6]
#
#Explanation:
#KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
#kthLargest.add(3);   // return 3
#kthLargest.add(5);   // return 3
#kthLargest.add(6);   // return 3
#kthLargest.add(7);   // return 5
#kthLargest.add(8);   // return 6
#
# Can use a regular min heap.
# Can iterate over nums O(N), while continously pushing to our min heap, but 
# ONLY if the current value to be pushed is GREATER than the current min value
# The min value would be identified by the first element of the heap (heap[0])
import heapq

class KthLargest:
  def __init__(self, k: int, nums: list[int]):
    self.heap = []
    self.k: int = k

    for num in nums:
      self.add(num)

  def add(self, val: int) -> int:
    if len(self.heap) < self.k or val > self.heap[0]:
        heapq.heappush(self.heap, val)

    if len(self.heap) > self.k:
      heapq.heappop(self.heap)

    return self.heap[0]

  def __repr__(self) -> str:
    return self.heap.__repr__()

def main():
  kthLargest: KthLargest = KthLargest(3, [1, 2, 3, 3]);
  print(kthLargest)
  kthLargest.add(3);   # return 3
  kthLargest.add(5);   # return 3
  kthLargest.add(6);   # return 3
  kthLargest.add(7);   # return 5
  kthLargest.add(8);   # return 6
  pass


if __name__ == "__main__":
  main()
