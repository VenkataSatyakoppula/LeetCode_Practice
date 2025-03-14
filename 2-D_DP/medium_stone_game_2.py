class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        def dfs(alice,i,M):
            if i == len(piles):
                return 0
            if (alice,i,M) in cache:
                return cache[(alice,i,M)]
            res = 0 if alice else float("inf")
            total = 0
            for X in range(1,2*M+1):
                if i+X > len(piles):
                    break
                total += piles[i+X-1]
                if alice:
                    res = max(res,total + dfs(not alice,i+X,max(X,M)))
                else:
                    res = min(res,dfs(not alice,i+X,max(X,M)))
            cache[(alice,i,M)] = res
            return res
        
        return dfs(True,0,1)
