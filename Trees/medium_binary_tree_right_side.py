# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        q = deque()
        q.append(root)
        while(q):
            right = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    right=node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                final.append(right.val)
        return final
