from collections import deque,defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        if not edges:
            return [0]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        leaves = deque()
        edge_cnt = {}
        for node,nei in adj.items():
            if len(nei) == 1:
                leaves.append(node)
            edge_cnt[node] = len(nei)
        while leaves:
            if n <= 2:
                return list(leaves) 
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for nei in adj[leaf]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
        return []
