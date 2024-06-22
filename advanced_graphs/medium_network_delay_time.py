class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        #Dijkstra's Algorithm
        minHeap = [(0,k)]
        t = 0
        visit = set()
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(w1,t)
            for n2,w2 in graph[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w2+w1,n2))
        return t if len(visit) == n else -1
