import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n_small = heapq.nsmallest(k,[-val for val in nums])
        return -1*n_small[k-1]
