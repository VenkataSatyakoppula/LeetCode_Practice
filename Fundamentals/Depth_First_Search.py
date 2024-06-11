from collections import deque

"""
S: [C, A, L]
C: [S, R]
A: [S, R]
L: [S, R]
R: [L, A, C]
"""
graph = {

'S': set(['C', 'A', 'L']),
'C': set(['S', 'R']),
'A': set(['S', 'R']),
'L': set(['S', 'R']),
'R': set(['L', 'A', 'C'])

}
visited = set()
graph_keys = list(graph.keys())
def dfs_recursive(v):
    visited.add(v)
    print(v,end=" ")
    for child in graph[v]:
        if child not in visited:
            dfs_recursive(child)

def dfs_iterative(start):
    visited.add(start)
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        print(node, end=" ")
        for child in graph[node]:
            if child not in visited:
                stack.append(child)
                visited.add(child)


print(dfs_recursive('S'))
visited.clear()
print(dfs_iterative('S'))


