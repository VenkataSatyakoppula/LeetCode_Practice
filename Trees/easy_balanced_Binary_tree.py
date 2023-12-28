# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth =[0]
        def dfs(root):
            if not root:
                return 0
            left,right = dfs(root.left),dfs(root.right)
            depth[0] = max(depth[0],abs(left-right))
            return 1+ max(left,right)
        dfs(root)
        if depth[0]<=1:
            return True
        return False  
