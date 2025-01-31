class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L = max(weights)
        R = sum(weights)
        def satisfies(capacity):
            cnt = 1
            t = capacity
            for i in range(len(weights)):
                if t - weights[i] < 0:
                    cnt +=1
                    t = capacity
                t -= weights[i]
            return cnt <= days
        res = R
        while(L <= R):
            mid = (L + R)// 2
            if satisfies(mid):
                res = min(mid,res)
                R = mid -1
            else:
                L = mid + 1
        
        return res
