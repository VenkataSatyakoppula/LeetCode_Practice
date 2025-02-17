class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        trips.sort(key=lambda x:x[1])
        cur_cap = 0
        for t in trips:
            numPass,start,end = t

            while minHeap and minHeap[0][0] <= start:
                cur_cap -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            cur_cap += numPass
            if cur_cap > capacity:
                return False
            heapq.heappush(minHeap,[end,numPass])
        return True
