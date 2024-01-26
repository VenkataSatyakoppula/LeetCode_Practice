class Solution:
    def isHappy(self, n: int) -> bool:
        tot = n
        def getDigits(n: int):
            digits = []
            while(n>=1):
                rem = n%10
                n = n//10
                digits.append(rem)
            return digits
        while(tot!=1):
            digits = getDigits(tot)
            tot =0
            for num in digits:
                tot += num*num
        return True

if __name__ == "__main__":
     sol = Solution()
     print(sol.isHappy(19))
