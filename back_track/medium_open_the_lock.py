class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1
        
        def children(val):
            res = []
            for i in range(4):
                digit = str((int(val[i]) + 1 )% 10)
                res.append(val[:i]+digit+val[i+1:])
                digit = str((int(val[i]) - 1 + 10)% 10)
                res.append(val[:i]+digit+val[i+1:])
            return res

        q = deque()
        visit = set(deadends)
        q.append(["0000",0])
        while q:
            val,turns = q.popleft()
            if val == target:
                return turns
            
            for child in children(val):
                if child not in visit:
                    visit.add(child)
                    q.append([child,turns+1])

        return -1
