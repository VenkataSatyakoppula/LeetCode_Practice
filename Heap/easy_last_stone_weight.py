import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones)>1:
            first = heapq.heappop(neg_stones)
            second = heapq.heappop(neg_stones)
            if first<second:
                heapq.heappush(neg_stones,first-second)
        neg_stones.append(0)
        return abs(neg_stones[0])
