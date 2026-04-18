class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i, j, index):
            if index==len(word):
                return True

            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or visited[i][j] or board[i][j]!=word[index]:
                return False
            visited[i][j]=True
            if (search(i-1, j, index+1) or
                search(i+1, j, index+1) or 
                search(i, j+1, index+1) or
                search(i, j-1, index+1)                
            ):
                return True

            visited[i][j]=False
            return False




        row,col = len(board), len(board[0])
        visited = [[False] * col for _ in range(len(board))]
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0] and search(i,j, 0):
                    return True
        return False

        
            