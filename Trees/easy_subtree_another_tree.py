# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if not p and not q :
                return True
            if not p or not q:
                return False
            if p and q and (p.val != q.val):
                return False
            left = isSameTree(p.left,q.left)
            right = isSameTree(p.right,q.right)
            return left and right 
        if not subRoot:
            return True
        if not root:
            return False
        
        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
