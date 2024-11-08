class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        start=0
        end=0
        cnt = 0
        res = []
        for i in s:
            start +=1
            end = max(lastIndex[i],end)
            if cnt == end:
                res.append(start)
                start=0
            cnt+=1
        return res
