#
# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
#
# Return the k closest points to the origin (0, 0).
#
# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
#
# You may return the answer in any order.
#
# Loop through points and convert points[i] to a Euclidean distance from the origin
# Add all those values to a min heap
# return top three values
import math
import heapq


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    distances: list[tuple] = []
    res = []

    for point in points:
        x1, y1, x2, y2 = 0, 0, point[0], point[1]
        distance = float(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
        heapq.heappush(distances, (distance, [x2, y2]))

    for _ in range(k):
        _, coord = heapq.heappop(distances)
        res.append(coord)

    return res


def main():
    print("--")
    print(kClosest([[0, 2], [2, 2]], 1))
    print(kClosest([[0, 2], [2, 0], [2, 2]], 2))


if __name__ == "__main__":
    main()
