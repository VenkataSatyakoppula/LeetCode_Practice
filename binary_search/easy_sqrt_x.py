class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 1):
            return 1
        l , r = 0 , x // 2

        while(l <= r):
            m = (l+r) // 2
           
            if m**2 == x:
                return m
            if m**2 < x:
                l = m + 1
            else:
                r = m - 1
        
        return l - 1
        
