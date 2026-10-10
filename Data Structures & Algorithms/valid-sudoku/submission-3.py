class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rowset = set()
            for j in range(len(board[i])):
                cell = board[i][j]
                if cell == ".":
                    continue
                elif cell in rowset:
                    return False
                else:
                    rowset.add(cell)

        for j in range(len(board[0])):
            colset = set()
            for i in range(len(board)):
                cell = board[i][j]
                if cell == ".":
                    continue
                elif cell in colset:
                    return False
                else:
                    colset.add(cell)

        direction = [(0,0), (0,3), (0,6),
                     (3,0), (3,3), (3,6),
                     (6,0), (6,3), (6,6)]

        for x,y in direction:
            squareset = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    cell = board[i][j]
                    if cell == ".":
                        continue
                    elif cell in squareset:
                        return False
                    else:
                        squareset.add(cell)

        return True

        



                