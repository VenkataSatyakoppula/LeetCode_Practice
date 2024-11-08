class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_list = []

        for i in range(len(intervals)):
            if(newInterval[1]<intervals[i][0]):
                new_list.append(newInterval)
                return new_list+intervals[i:]
            elif(newInterval[0]>intervals[i][1]):
                new_list.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
        new_list.append(newInterval)
        return new_list
