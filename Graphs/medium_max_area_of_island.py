class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r,c):
            q = collections.deque()
            local_area = 1
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col = q.pop()
                direc = [[0,1],[0,-1],[1,0],[-1,0]]
                for i,j in direc:
                    dr,dc = row+i,col+j
                    if(dr in range(rows) and 
                    dc in range(cols) and 
                    grid[dr][dc] == 1 and 
                    (dr,dc) not in visited):
                        q.append((dr,dc))
                        visited.add((dr,dc))
                        local_area += 1
            return local_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(dfs(i,j),max_area)
        
        return max_area
