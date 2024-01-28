class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = bin(n)
        return bin_str.count('1')
    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while(n):
            res += n % 2
            n = n>>1
        return res 

if __name__ == "__main__":
     a = Solution()
     print(a.hammingWeight2(3))
