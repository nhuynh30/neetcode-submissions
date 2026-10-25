class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        hi = len(matrix)*len(matrix[0])-1
        rows = len(matrix)
        cols = len(matrix[0])
        while low<=hi:
            mid = low + (hi-low)//2
            row = mid//cols
            col= mid%cols
            val = matrix[row][col]
            if val == target:
                return True
            elif val<target:
                low=mid+1
            else:
                hi=mid-1
        
        return False

