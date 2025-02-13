class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a>0:
            heapq.heappush(maxHeap,[-a,'a'])
        if b>0:
            heapq.heappush(maxHeap,[-b,'b'])
        if c>0:
            heapq.heappush(maxHeap,[-c,'c'])
        prev , res = None,""
        while maxHeap:
            cnt , char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                cnt2 , char2 = heapq.heappop(maxHeap)
                cnt2 += 1
                res += char2
                if cnt2 !=0:
                    heapq.heappush(maxHeap,[cnt2,char2])
            else:
                cnt += 1
                res += char
            if cnt != 0:
                heapq.heappush(maxHeap,[cnt,char])
            
        return res

