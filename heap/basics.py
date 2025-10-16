# Support two operations
# heap pop, heap push
# heapify is a function that implements 'sift_down' O(N) time, O(N) space

import heapq


def heapsort(arr: list) -> list:
    heapq.heapify(arr)  # min heap by default
    n = len(arr)
    res: list = [0] * n

    for i in range(n):
        min = heapq.heappop(arr)
        res[i] = min

    return res


def maxheapsort(arr: list) -> list:
    n = len(arr)
    # Negate all values
    for i in range(n):
        arr[i] = -arr[i]

    heapq.heapify(arr)

    res: list = [0] * n
    for i in range(len(res)):
        res[i] = -(heapq.heappop(arr))

    return res


def main():
    A: list = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
    heapq.heapify(A)
    print(A)

    B: list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(heapsort(B))  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    C: list = [3, 5, 1, 76, 3, 456, 7, 2, 4]
    print(maxheapsort(C))

    list_of_tupleS: list[tuple] = [(7, 3), (1, 2), (1, 3), (4, 5)]

    heapq.heapify(list_of_tupleS)

    # prints [(1, 2), (4, 5), (1, 3), (7, 3)]
    # (1,3) is the left child of (1,2) if the first value from
    # left to right is the same
    print(list_of_tupleS)


if __name__ == "__main__":
    main()
