class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append([dist,j])
                graph[j].append([dist,i])
        
        #prim's algo O(n^2 log(n))
        visit = set()
        minH = [[0,0]]
        res = 0
        while len(visit) < len(points):
            dist, node = heapq.heappop(minH)
            if node in visit:
                continue
            res += dist 
            visit.add(node)
            for cost, nei in graph[node]:
                heapq.heappush(minH,[cost,nei])
        return res
