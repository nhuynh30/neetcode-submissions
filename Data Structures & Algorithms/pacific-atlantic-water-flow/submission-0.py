class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()

        def dfs(row, col, prev,visit):
            if row<0 or col<0 or row>=len(heights) or col>= len(heights[0]) or (row,col) in visit or heights[row][col]<prev:
                return 
            
            visit.add((row,col))
            dfs(row-1, col, heights[row][col], visit)
            dfs(row+1, col, heights[row][col], visit)
            dfs(row, col-1, heights[row][col], visit)
            dfs(row, col+1, heights[row][col], visit)

        for row in range(len(heights)):
            dfs(row, 0, 0, pacific)
            dfs(row, len(heights[0])-1, 0, atlantic)

        for col in range(len(heights[0])):
            dfs(0, col, 0, pacific)
            dfs(len(heights)-1, col, 0, atlantic)

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row,col) in pacific and (row,col) in atlantic:
                    res.append((row,col))

        return res


