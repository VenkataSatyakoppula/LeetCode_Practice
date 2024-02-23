class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*len(temperatures)
        for index,temp in enumerate(temperatures):
            while stk and (temp>stk[-1][0]):
                ele,i = stk.pop()
                res[i] = index-i
            stk.append([temp,index])
        return res
