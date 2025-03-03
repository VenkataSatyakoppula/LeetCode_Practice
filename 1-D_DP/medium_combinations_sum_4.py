class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(cnt):
            if cnt in cache:
                return cache[cnt]
            if cnt == target:
                return 1
            if cnt > target:
                return 0
            res = 0
            for j in range(len(nums)):
                res += dfs(cnt+nums[j])
            cache[cnt] = res
            return cache[cnt]
        
        return dfs(0)

