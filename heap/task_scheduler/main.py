#You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
#
#Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
#
#The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
#
#Return the minimum number of CPU cycles required to complete all tasks.
#
#Example 1:
#
#Input: tasks = ["X","X","Y","Y"], n = 2
#
#Output: 5
#
#Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.
#
#Example 2:
#
#Input: tasks = ["A","A","A","B","C"], n = 3
#
#Output: 9
#
#Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

# We need to determine the most optimal sequence of indexes in tasks such that the CPU
# idles as little as possible.
# An idle happens if identical tasks are not separate by at least 'n' CPU cycles.
#
# What if we use a min heap to store the ord(c) where c == tasks[i]
#
# We can keep track of the lask task scheduled (last_scheduled = ord(task[i]))
#
# While the heap is non empty, and the current min value == last_scheduled, pop from the heap and store those
# values temporarily in 'to_be_processed: list or queue'??
#
# after finding a valid task to schedule, pop it, increase CPU cycles res variable, and then push ONE task from to_be_processed back onto the heap
# 
# Repeat that whole process until the heap is empty.
#
# If the heap is empty, but to_be_processed is full, there must be leftover elements that couldn't be processed in round robin with something else. Will have to increment cycles  += n * len(to_be_processed) before returning cycles

import heapq

def leastInterval(tasks: List[str], n: int) -> int:
  # convert to ASCII
  tasks = [ord(t) for t in tasks]

  tasks = heapq.heapify(tasks)

def main():
  print(leastInterval(["x","x","y","y"], 2))

if __name__ == "__main__":
  main()
