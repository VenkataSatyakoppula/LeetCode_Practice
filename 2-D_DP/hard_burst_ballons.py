class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        
        def dfs(l,r):
            if  l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            print(dp)
            for i in range(l,r+1):
                res = nums[l-1]*nums[i]*nums[r+1]
                res += dfs(l,i-1)+dfs(i+1,r)
                dp[(l,r)] = max(res,dp[(l,r)])
            return dp[(l,r)]
        return dfs(1,len(nums)-2)
