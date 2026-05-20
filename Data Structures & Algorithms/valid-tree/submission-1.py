class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        adjList = {i: [] for i in range(n)}

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in adjList[node]:
                dfs(neigh)

        dfs(0)

        return len(visited)==n
