# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
#
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
#
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
#
# Return the minimum number of CPU cycles required to complete all tasks.
#
# Example 1:
#
# Input: tasks = ["X","X","Y","Y"], n = 2
#
# Output: 5
#
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.
#
# Example 2:
#
# Input: tasks = ["A","A","A","B","C"], n = 3
#
# Output: 9
#
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

# We need to determine the most optimal sequence of indexes in tasks such that the CPU
# idles as little as possible.
# An idle happens if identical tasks are not separate by at least 'n' CPU cycles.
#
# What if we use a min heap to store the ord(c) where c == tasks[i]
#
# We can keep track of the last task scheduled (last_scheduled = ord(task[i]))
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
import collections


def leastInterval(tasks: list[str], n: int) -> int:
    time = 0
    queue = collections.deque()
    counts = collections.Counter(tasks)
    count_heap = []

    # Get frequencies, build heap
    for count in counts.values():
        heapq.heappush(count_heap, -count)

    while len(queue) > 0 or len(count_heap) > 0:
        print("queue: ", queue)
        print("heap: ", count_heap)

        if len(queue) > 0 and queue[0][1] == time:
            # more efficient that individual push and pop
            cur_task = heapq.heappushpop(count_heap, queue.popleft()[0])
        elif len(count_heap) > 0:
            cur_task = heapq.heappop(count_heap)
        else:
            time += 1
            continue

        # Schedule 1 task
        cur_task += 1

        if cur_task != 0:
            available_at = time + n + 1
            queue.append((cur_task, available_at))

        time += 1

    return time


def main():
    print(leastInterval(["x", "x", "y", "y"], 2))
    print()
    print(leastInterval(["A", "A", "A", "B", "C"], 3))
    print()


if __name__ == "__main__":
    main()
