class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visit = set()
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for n in graph[i]:
                dfs(n)
        connected = 0
        for node in graph:
            if node not in visit:
                dfs(node)
                connected +=1
        return connected

