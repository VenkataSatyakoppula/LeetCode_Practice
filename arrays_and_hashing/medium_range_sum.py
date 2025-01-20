class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS , COLS = len(matrix) , len(matrix[0])
        self.summat = [[0]*(COLS+1) for r in range(ROWS+1)]
        for i in range(ROWS):
            left = 0
            for j in range(COLS):
                left += matrix[i][j]
                top = self.summat[i][j+1]
                self.summat[i+1][j+1] = left + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1

        topright = self.summat[row1 - 1][col2]
        bottomleft = self.summat[row2][col1 - 1]
        topleft = self.summat[row1-1][col1-1] 
        return self.summat[row2][col2] - topright - bottomleft + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
