"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoNew = {}
        def bfs(n):
            if n in oldtoNew:
                return oldtoNew[n]
            clone = Node(n.val)
            oldtoNew[n] = clone
            for nei in n.neighbors:
                clone.neighbors.append(bfs(nei))

            return clone
        return bfs(node) if node else None
