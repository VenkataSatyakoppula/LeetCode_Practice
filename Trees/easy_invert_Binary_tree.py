# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion approach
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        left = root.left
        root.left = root.right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
# Iterative approach
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            node.left,node.right = node.right,node.left
        return root
