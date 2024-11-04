from operator import itemgetter
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s_inter = sorted(intervals,key=itemgetter(0))
        cnt = 0
        # working code (own)
        # i , j=0,1 
        # while(i< len(s_inter)):
        #     cur = s_inter[i]
        #     if(i == j):
        #         j = i+1
        #     if( j < len(s_inter) and cur[1] > s_inter[j][0]):
        #         if(cur[1] > s_inter[j][1]):
        #             i = j
        #         else:
        #             j = j+1
        #         cnt +=1
        #     else:
        #         i = j
        prevEnd = s_inter[0][1]
        for start,end in s_inter[1:]:
            if(start>=prevEnd):
                prevEnd = end
            else:
                cnt+=1
                prevEnd = min(prevEnd,end)
        return cnt
