class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        border = set()
        def dfs(row, col, visit):
            if row<0 or col<0 or row>= len(board) or col>= len(board[0]) or (row, col) in border or board[row][col]=='X' or visited[row][col]:
                return
            visit.add((row, col))
            visited[row][col] = True

            dfs(row+1, col, visit)
            dfs(row-1, col, visit)
            dfs(row, col+1, visit)
            dfs(row, col-1, visit)

        for i in range(len(board)):
            dfs(i, 0, border)
            dfs(i, len(board[0])-1, border)

        for j in range(len(board[0])):
            dfs(0, j, border)
            dfs(len(board)-1, j, border)

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O' and (i,j) not in border:
                    board[i][j]='X'

        