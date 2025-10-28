#You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
#
#    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#
#There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
#
#Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

from collections import defaultdict

def findOrder(numCourse: int, prerequisites: list[list[int]]) -> list[int]:
    prereq = { c: [] for c in range(numCourse)}

    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output: list[int] = []
    visit: set[int] = set()
    cycle: set[int] = set()

    def dfs(crs) -> bool:
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if not dfs(pre):
                return False

        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourse):
        if not dfs(c):
            return []

    return output

def main():
    prerequisites=[[0,1]]
    print(findOrder(3,prerequisites))


if __name__ == "__main__":
    main()
