class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS , COLS = len(matrix), len(matrix[0])
        dp = [[0]*COLS for i in range(ROWS)]
        maxRes = 0

        def dfs(r,c,preval):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= preval
               ):
               return 0

            if dp[r][c] != 0:
                return dp[r][c]
            res = 1
            res = max(res,dfs(r + 1,c,matrix[r][c]) + 1)
            res = max(res,dfs(r,c+1,matrix[r][c]) + 1)
            res = max(res,dfs(r,c-1,matrix[r][c]) + 1)
            res = max(res,dfs(r-1,c,matrix[r][c]) + 1)
            dp[r][c] = res
            return res

        for i in range(ROWS):
            for j in range(COLS):
                maxRes = max(maxRes,dfs(i,j,-1))
        return maxRes

