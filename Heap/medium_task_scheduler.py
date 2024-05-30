import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        heap = [-val for val in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time +=1
            if heap:
                ele = heapq.heappop(heap)
                ele += 1
                if ele:
                    q.append([ele,time+n])
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
        return time
