# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root -> left -> right
        res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        #dfs(root)
        # Iterative solution
        stack = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
            
        return res
