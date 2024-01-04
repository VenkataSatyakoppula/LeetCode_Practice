class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one,two = 1,1

        for i in range(n):
            temp = two
            two = one+two
            one = temp
        return one
    
