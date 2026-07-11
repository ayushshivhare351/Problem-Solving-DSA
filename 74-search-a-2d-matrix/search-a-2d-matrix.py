class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i,j = 0,(m*n)-1
        while i<=j:
            mid = (i+j)//2
            if matrix[mid//n][mid%n]<target:
                i+=1
            elif matrix[mid//n][mid%n]> target:
                j-=1
            else:
                return True
        return False
            