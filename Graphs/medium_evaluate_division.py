class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append([equations[i][1],values[i]])
            adj[equations[i][1]].append([equations[i][0],1/values[i]])
        
        def bfs(start,target):
            if start not in adj or target not in adj:
               return -1
            q, visit = deque(), set()
            q.append([start,1])
            while q:
                node , w = q.popleft()
                visit.add(node)
                if node==target:
                    return w
                for child,weight in adj[node]:
                    if child not in visit:
                        q.append([child,w*weight])     
            return -1
        
        return [bfs(a,b) for a,b in queries]

