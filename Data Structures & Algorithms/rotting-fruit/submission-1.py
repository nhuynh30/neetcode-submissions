class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        level = deque()
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    level.append((i,j))

        queue.append(level)

        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        res = -1
        while queue:
            level = queue.popleft()
            res+=1
            newlevel = deque()
            for _ in range(len(level)):
                i, j = level.popleft()
                for rc, cc in direction:
                    nr = i+rc
                    nc = j+cc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        newlevel.append((nr,nc))

            if len(newlevel)>0:
                queue.append(newlevel)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return res
