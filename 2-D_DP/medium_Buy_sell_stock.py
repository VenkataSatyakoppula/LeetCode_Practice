class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i + 1 for buy
        # i + 2 for sell because of cooldown

        dp = {} # key = (i,buying) val = max profit

        def dfs(i,buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            cooldown = dfs(i+1,buying)
            if buying:
                buy = dfs(i+1,not buying) - prices[i]
                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2,not buying) + prices[i]
                dp[(i,buying)] = max(sell,cooldown)
            return dp[(i,buying)]
        return dfs(0,True)
