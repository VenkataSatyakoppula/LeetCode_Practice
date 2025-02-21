class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {c+1:[] for c in range(n)}
        for a,b in trust:
            graph[a].append(b)
        judge = -1
        for key in graph:
            if len(graph[key]) == 0:
                judge = key
        for key in graph:
            if key != judge and judge not in graph[key]:
                return -1
        return judge
