class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False]* len(grid[0]) for _ in range(len(grid))]
        res = 0
        def dfs(row, col):
            if row<0 or col <0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]==0 or visited[row][col]:
                return 0
            area = 1
            visited[row][col] = True
            area += dfs(row+1, col)
            area += dfs(row-1, col)
            area += dfs(row, col+1)
            area += dfs(row, col-1)

            return area

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]==1:
                    res = max(res, dfs(i,j))

        return res
