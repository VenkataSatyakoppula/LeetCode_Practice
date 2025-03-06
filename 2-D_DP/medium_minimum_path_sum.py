class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i<0 or j<0 or i == n or j == m:
                return float("inf")
            if i == n-1 and j== m-1:
                return grid[i][j]
            res = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1)) 
            cache[(i,j)] = res
            return res
        return dfs(0,0)
