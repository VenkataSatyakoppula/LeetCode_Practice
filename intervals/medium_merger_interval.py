from operator import itemgetter
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    
        
        sorted_intervals = sorted(intervals,key=itemgetter(0))
        res = [sorted_intervals[0]]
        #Commented code works too (my own)
        # cur = sorted_intervals[0]
        # for i in range(1,len(intervals)):
        #     if(cur[1] >= sorted_intervals[i][0]):
        #         if(cur[0]> sorted_intervals[i][1]):
        #             res.append(cur)
        #             cur = sorted_intervals[i]
        #         cur = [min(cur[0],sorted_intervals[i][0]),max(cur[1],sorted_intervals[i][1])]
        #     else:
        #         res.append(cur)
        #         cur = sorted_intervals[i]
        #res.append(cur)
        for start,end in sorted_intervals:
            lastend = res[-1][1]
            if start <= lastend:
                res[-1][1] = max(end,lastend)
            else:
                res.append([start,end])
        return res
