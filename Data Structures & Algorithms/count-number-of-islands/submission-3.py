class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0

        def dfs(r, c, visited):
            if r<0 or c<0 or r>=len(visited) or c>=len(visited[0]) or visited[r][c] or grid[r][c]=="0":
                return
            visited[r][c] = True
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if not visited[r][c] and grid[r][c]=="1":
                    dfs(r,c, visited)
                    res+=1

        return res


    