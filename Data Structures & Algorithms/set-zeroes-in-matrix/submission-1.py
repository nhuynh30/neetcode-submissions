class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setRow = set()
        setCol = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    setRow.add(i)
                    setCol.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in setRow or j in setCol:
                    matrix[i][j] = 0

            
        