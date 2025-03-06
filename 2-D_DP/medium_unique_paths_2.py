class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i < 0 or j < 0 or i == n or j == m or obstacleGrid[i][j] == 1:
                return 0
            if i == n-1 and j == m-1:
                return 1
            res = 0
            res += dfs(i+1,j)
            res += dfs(i,j+1)
            cache[(i,j)] = res
            return res
        return dfs(0,0)
