class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(len(board)):
            rowSet = set()
            for col in range(len(board[row])):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rowSet:
                    return False
                rowSet.add(val)

        for col in range(len(board[0])):
            colSet = set()
            for row in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue
                if val in colSet:
                    return False
                colSet.add(val)
        
        matrix = [(0,0), (3,0), (6,0),
                   (0,3), (3,3), (6,3),
                   (0,6), (3,6), (6,6)]
    
        for i,j in matrix:
            squareSet = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in squareSet:
                        return False
                    squareSet.add(val)

        return True
                    


