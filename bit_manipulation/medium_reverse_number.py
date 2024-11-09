class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        t2 = abs(x)
        MAX = 2147483647
        MIN = -217483648
        while(t2 >0):
            rem =  t2 % 10
            t2 = t2 //10
            res = res*10 + rem
        
        if res <= MIN or res >= MAX:
            return 0
        if(x<0):
            return -1*res
        return res
