class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+","-","*","/"]
        stk = []
        def do_op(num1,num2,op):
            if op == "+":
                return num2+num1
            elif op =="-":
                return num2-num1
            elif op == "*":
                return num2*num1
            else:
                return int(num2/num1)
        for token in tokens:
            if token in ops:
                num1 = stk.pop()
                num2 = stk.pop()
                stk.append(do_op(num1,num2,token))
            else:
                stk.append(int(token))
        return stk.pop()
