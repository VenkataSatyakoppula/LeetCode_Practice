#LeetCode Premium problem template taken from Lintcode

from typing import (
    List,
)

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda l:l.start)
        end = intervals[0].end
        i = 1
        while(i<len(intervals)):
            if end<= intervals[i].end:
                end = intervals[i].end
            else:
                return False
            i +=1
        return True

if __name__ == "__main__":
    sol = Solution()
    test1 = [Interval(0,30),Interval(5,10),Interval(15,20)]
    test2 = [Interval(5,8),Interval(9,15)]
    print("Testcase-1: ",sol.can_attend_meetings(test1) == False)
    print("Testcase-2: ",sol.can_attend_meetings(test2) == True)
