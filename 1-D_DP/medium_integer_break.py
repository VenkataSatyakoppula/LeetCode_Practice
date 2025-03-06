class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}
        def dfs(num):
            if num in cache:
                return cache[num]
            if num == 0:
                return 1
            if num < 0 :
                return -1
            max_prod = 1
            for i in range(1,n):
                max_prod =  max(max_prod,i*dfs(num-i))
            cache[num] = max_prod
            return max_prod
        return dfs(n)
