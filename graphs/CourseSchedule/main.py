#Yo[=eryp]u are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
#
#The pair [0, 1], indicates that must take course 1 before taking course 0.
#
#There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
#
#Return true if it is possible to finish all courses, otherwise return false.
#
# 1. Break our 2D array into a directed graph map object
# 2. DFS from start node (how to find? iterate through all nodes?)
# 3. If node has already been seen, return False
# 4. If never return Return false, return True if len(seen) >= numCourse

from Intro.main import convert_edges_list_to_adj_map

def canFinish(numCourse: int, prerequisites: list[list[int]]) -> bool:
    # 1.
    adj_map = convert_edges_list_to_adj_map(prerequisites)
    num_nodes_seen: set[int] = set()

    def dfs(node: int, seen: set[int]) -> bool:
        # Need this for counting at end
        if node not in num_nodes_seen:
            num_nodes_seen.add(node)

        # 3. 
        if node in seen:
            return False

        seen.add(node)

        if node not in adj_map:
            seen.remove(node)
            # End node, doesn't have any edges to anyone
            return True

        for neighbor in adj_map[node]:
            if not dfs(neighbor, seen):
                seen.remove(node)
                return False

        seen.remove(node)

        return True
    # 2. 
    for node in adj_map.keys():
        res = dfs(node, set())
        if not res:
            return False

    return len(num_nodes_seen) >= numCourse

def main():
    prerequisites=[[1,4],[2,4],[3,1],[3,2]]
    print(canFinish(5,prerequisites))


if __name__ == "__main__":
    main()
