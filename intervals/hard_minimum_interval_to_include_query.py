class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        minHeap = []
        i=0
        for query in sorted(queries):
            while i < len(intervals) and query >= intervals[i][0]:
                heapq.heappush(minHeap,(intervals[i][1] - intervals[i][0] + 1,intervals[i][1]))
                i+=1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            res[query] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
                        
