class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        carry = 0
        res = 0
        for i in range(len(num2)-1,-1,-1):
            inter = 0
            for j in range(len(num1)-1,-1,-1):
               multi = int(num1[j])*int(num2[i]) + carry
               carry = multi // 10
               inter +=  (10**(len(num1)-1-j))*(multi%10)
            if(carry!=0):
                inter += (10**(len(num1)))*carry
                carry =0
            res += (10**(len(num2)-1-i))*(inter)

        return str(res)

