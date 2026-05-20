class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        count = 0
        visited = set()

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neigh in adjList[node]:
                dfs(neigh)

        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)

        return count