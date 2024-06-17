class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for sub in prerequisites:
            graph[sub[0]].append(sub[1])
        visit = set()
        def dfs(v):
            if v in visit:
                return False
            if graph[v] == []:
                return True
            visit.add(v)
            for child in graph[v]:
                if not dfs(child):
                    return False
            visit.remove(v)
            graph[v] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

