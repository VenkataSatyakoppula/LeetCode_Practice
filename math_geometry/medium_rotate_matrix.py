class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix) - 1

        while(l<r):
            for i in range(r-l):
                top, bottom = l,r
                topleft = matrix[top][l+i]

                #swap bottom left to top left
                matrix[top][l+i] =  matrix[bottom-i][l] 

                #swap bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #swap top right with bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #swap top left with top right
                matrix[top+i][r] = topleft
            l +=1
            r -=1
