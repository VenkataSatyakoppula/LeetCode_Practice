class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMin,globMax = nums[0] , nums[0]
        curMin,curMax = 0 , 0
        total = 0
        for n in nums:
            curMin = min(curMin+n,n)
            curMax = max(curMax+n,n)
            total +=n
            globMin = min(globMin,curMin)
            globMax = max(globMax,curMax)
        
        return max(globMax,total-globMin) if globMax > 0 else globMax
