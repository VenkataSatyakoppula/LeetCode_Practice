class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-cnt,val] for val,cnt in counts.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt , val = heapq.heappop(maxHeap)
            cnt += 1
            res += val
            
            if prev:
                heapq.heappush(maxHeap,prev)
                prev= None
            if cnt !=0:
                prev = [cnt,val]

        return res

