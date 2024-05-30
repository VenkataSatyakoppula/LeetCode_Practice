import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap_list = []
        for x,y in points:
            dist = x*x + y*y
            heap_list.append([dist,x,y])
        
        heapq.heapify(heap_list)
        res = []
        while k>0:
            dist,x,y = heapq.heappop(heap_list)
            res.append([x,y])
            k -=1
        return res
