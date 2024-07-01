class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for d in dp:
                nextDp.add(d+nums[i])
                nextDp.add(d)
            dp = nextDp
        return  True if target in dp else False
