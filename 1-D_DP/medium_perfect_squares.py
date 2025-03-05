class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dfs(rem):
            if rem in cache:
                return cache[rem]
            if rem == 0:
                return 0
            min_len = rem
            for i in range(1,rem+1):
                if i*i > rem:
                    break 
                min_len = min(min_len,1+dfs(rem - i*i))
            cache[rem] = min_len
            return cache[rem]
        return dfs(n)
