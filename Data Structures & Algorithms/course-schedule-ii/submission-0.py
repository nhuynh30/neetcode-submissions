class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adjList = {i: [] for i in range(numCourses)}
        for crs, prev in prerequisites:
            adjList[crs].append(prev)

        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for neigh in adjList[crs]:
                if not dfs(neigh):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []



        return res