class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights), len(heights[0])
        visit = set()
        directions= [[0,1],[1,0],[-1,0],[0,-1]]
        minHeap = [[0,0,0]]
        while minHeap:
            diff, r ,c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            if (r,c) == (n-1,m-1):
                return diff
            visit.add((r,c))
            for dr,dc in directions:
                newR , newC = r+dr,c+dc
                if newR <0 or newC <0 or newR == n or newC == m or (newR,newC) in visit:
                    continue
                new_diff = max(diff,abs(heights[newR][newC]-heights[r][c]))
                heapq.heappush(minHeap,[new_diff,newR,newC])
